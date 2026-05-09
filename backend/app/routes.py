from fastapi import APIRouter, HTTPException
from typing import List

from app import schemas
from app import firestore_service

router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)


@router.post("/", response_model=schemas.ApplicationResponse)
def create_application(application: schemas.ApplicationCreate):
    return firestore_service.create_application(application)


@router.get("/", response_model=List[schemas.ApplicationResponse])
def get_applications():
    return firestore_service.get_applications()


@router.get("/{application_id}", response_model=schemas.ApplicationResponse)
def get_application(application_id: str):
    application = firestore_service.get_application(application_id)

    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    return application


@router.put("/{application_id}", response_model=schemas.ApplicationResponse)
def update_application(
    application_id: str,
    application_data: schemas.ApplicationUpdate
):
    update_data = application_data.model_dump(exclude_unset=True)

    application = firestore_service.update_application(
        application_id,
        update_data
    )

    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    return application


@router.delete("/{application_id}")
def delete_application(application_id: str):
    deleted = firestore_service.delete_application(application_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Application not found")

    return {"message": "Application deleted successfully"}
