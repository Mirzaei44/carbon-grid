from celery import shared_task
from core.services.carbon_api import fetch_current_intensity
from core.services.ingestion import save_intensity_payload


@shared_task
def ingest_current_intensity_task():
    payload = fetch_current_intensity()
    saved = save_intensity_payload(payload)
    return {"saved": saved}
