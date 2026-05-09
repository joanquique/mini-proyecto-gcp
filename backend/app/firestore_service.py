from datetime import datetime, timezone
from typing import Optional
from google.cloud import firestore


db = firestore.Client()
applications_collection = db.collection("applications")


def serialize_application(doc):
    data = doc.to_dict()

    return {
        "id": doc.id,
        "company": data.get("company"),
        "position": data.get("position"),
        "status": data.get("status", "Pendiente"),
        "notes": data.get("notes"),
        "created_at": data.get("created_at"),
    }


def create_application(application):
    created_at = datetime.now(timezone.utc).isoformat()

    data = {
        "company": application.company,
        "position": application.position,
        "status": application.status,
        "notes": application.notes,
        "created_at": created_at,
    }

    doc_ref = applications_collection.document()
    doc_ref.set(data)

    return {
        "id": doc_ref.id,
        **data,
    }


def get_applications():
    docs = applications_collection.order_by(
        "created_at",
        direction=firestore.Query.DESCENDING
    ).stream()

    return [serialize_application(doc) for doc in docs]


def get_application(application_id: str):
    doc = applications_collection.document(application_id).get()

    if not doc.exists:
        return None

    return serialize_application(doc)


def update_application(application_id: str, update_data: dict):
    doc_ref = applications_collection.document(application_id)
    doc = doc_ref.get()

    if not doc.exists:
        return None

    doc_ref.update(update_data)

    updated_doc = doc_ref.get()
    return serialize_application(updated_doc)


def delete_application(application_id: str):
    doc_ref = applications_collection.document(application_id)
    doc = doc_ref.get()

    if not doc.exists:
        return False

    doc_ref.delete()
    return True
