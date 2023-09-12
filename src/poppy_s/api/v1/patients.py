#!/bin/env python3

from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from poppy_s.lib.models import Patient, PatientRead, PatientCreate
from poppy_s.lib.container import globalContainer
from poppy_s.lib.database import database

def getRouter() -> APIRouter:

    router = APIRouter(prefix="/patient", tags=["api", "api/v1", "api/v1/patient", "patients"])

    @router.get("/", response_model=List[PatientRead])
    async def getPatients(
        *, 
        session: Session = Depends(database.get_session),
        offset: int = 0,
        limit: int = Query(default=100, lte=100)
    ):

        patients = session.exec(select(Patient).offset(offset).limit(limit)).all()
        return patients
        
     
    @router.post("/", response_model=PatientRead)
    async def createPatient(*, session: Session = Depends(database.get_session), patient: PatientCreate):
        db_patient = Patient.from_orm(patient)
        session.add(db_patient)
        session.commit()
        session.refresh(db_patient)
        return db_patient


    @router.get("/{patient_id}", response_model=PatientRead)
    async def getPatient(*, session: Session = Depends(database.get_session), patient_id: int):
        patient = session.get(Patient, patient_id)
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
        return patient

    # @router.post("/login")
    # async def loginUser():
    #     pass

    


    return router