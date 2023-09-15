#!/bin/env python3
from typing import cast

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session #, select

from datetime import datetime, timezone

from poppy_s.lib.database import database

from poppy_s.lib.models import (
    Prescription, 
    PrescriptionCreate, 
    PrescriptionReadFullData, 
    PrescriptionRead,
    PrescriptionsMedicationDosageCreate,
    PrescriptionsMedicationDosage,
    PrescriptionsMedicationDosageBaseWithMedicationID,
    Medication,
    MedicationRead,
    Interaction,
    PrescriptionValidationErrorsBase
)

from poppy_s.lib.helpers.plugin_helpers.medications import find_medication_by_name

# from poppy_s.lib.helpers.plugin_helpers.interactions import (
#     find_interactions_by_rxcui, 
#     # compile_interactions_warnings 
# )
from poppy_s.lib.helpers.plugin_helpers.validators import (
    compile_validator_s_warnings,
    validate_prescription
)

from poppy_s.api.v1.helper_generator import genRouter

def getRouter() -> APIRouter:

    router = genRouter(
        "prescription", "prescriptions", "Prescription",
        Prescription, PrescriptionRead, PrescriptionReadFullData, PrescriptionCreate
    )

    @router.post("/{item_id}/add", response_model=PrescriptionReadFullData)
    async def addMedicationToPrescription(
        *, 
        session: Session = Depends(database.get_session), 
        item_id: int,
        medication_dosage: PrescriptionsMedicationDosageCreate,
        limit: int = Query(default=100, lte=500),
        loadmore: bool = Query(default=False)
    ):

        if item_id != medication_dosage.prescription_id:
            raise HTTPException(status_code=400, detail=f"Bad user input")

        
        prescription = session.get(Prescription, item_id)
        if not prescription:
            raise HTTPException(status_code=404, detail=f"Prescription not found")

        if prescription.sealed_at is not None:
            raise HTTPException(status_code=400, detail=f"Cannot Modify Sealed Prescription!")

        meds : list[Medication] = find_medication_by_name(
            session,
            name=medication_dosage.medication,
            num=limit,
            loadMore=loadmore
        )

        if len(meds) == 0:
            raise HTTPException(status_code=404, detail=f"Medication '{medication_dosage.medication}' not found")

        # Assumption: For now using the first on the returned list!

        med = MedicationRead.from_orm(meds[0])

        item = PrescriptionsMedicationDosageBaseWithMedicationID(medication_id=med.id, **medication_dosage.dict())

        db_item = PrescriptionsMedicationDosage.from_orm(item)
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
        session.refresh(prescription)

        return prescription

    @router.post("/{item_id}/close", response_model=PrescriptionReadFullData)
    async def closeMedicationToPrescription(
        *, 
        session: Session = Depends(database.get_session), 
        item_id: int,
        loadmore: bool = Query(default=False)
    ):
        
        prescription = session.get(Prescription, item_id)
        if not prescription:
            raise HTTPException(status_code=404, detail=f"Prescription not found")

        elif prescription.sealed_at is not None:
            raise HTTPException(status_code=400, detail=f"Prescription Already Sealed!")

        validation_errors = validate_prescription(
            session, 
            prescription=prescription,
            loadMore=loadmore
        )


        if len(validation_errors) > 0:
            # prescription.warnings.extend(warnings)

            # session.add(prescription)
            # session.commit()


            warnings = compile_validator_s_warnings(
                validation_errors,  
                asList=False
            )
            raise HTTPException(
                status_code=400, 
                detail=f"Unable to Seal Prescription with Warnings!\nWarnings:\n{warnings}"
            )

        
        prescription.sealed_at = datetime.now(timezone.utc)

        session.add(prescription)
        session.commit()
        session.refresh(prescription)

        return prescription

    return router
    

