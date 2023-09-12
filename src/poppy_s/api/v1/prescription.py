#!/bin/env python3

from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from poppy_s.lib.models import Prescription, PrescriptionRead, PrescriptionCreate
from poppy_s.lib.container import globalContainer
from poppy_s.lib.database import database

def getRouter() -> APIRouter:

    router = APIRouter(prefix="/doctor", tags=["api", "api/v1", "api/v1/doctor", "doctors"])

    @router.get("/", response_model=List[DoctorRead])
    async def getDoctors(
        *, 
        session: Session = Depends(database.get_session),
        offset: int = 0,
        limit: int = Query(default=100, lte=100)
    ):

        doctors = session.exec(select(Doctor).offset(offset).limit(limit)).all()
        return doctors
        
     
    @router.post("/", response_model=DoctorRead)
    async def createDoctor(*, session: Session = Depends(database.get_session), doctor: DoctorCreate):
        db_doctor = Doctor.from_orm(doctor)
        session.add(db_doctor)
        session.commit()
        session.refresh(db_doctor)
        return db_doctor


    @router.get("/{doctor_id}", response_model=DoctorRead)
    async def getDoctor(*, session: Session = Depends(database.get_session), doctor_id: int):
        doctor = session.get(Doctor, doctor_id)
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        return doctor

    # @router.post("/login")
    # async def loginUser():
    #     pass

    


    return router