from celery import shared_task
from django.core.mail import EmailMessage
from django.utils import timezone

from core.models import Report
from core.services.carbon_api import fetch_current_intensity
from core.services.ingestion import save_intensity_payload
from core.services.reporting import build_report_file


@shared_task
def ingest_current_intensity_task():
    payload = fetch_current_intensity()
    saved = save_intensity_payload(payload)
    return {"saved": saved}


@shared_task
def generate_report_task(report_id):
    report = Report.objects.get(id=report_id)
    report.status = "processing"
    report.save(update_fields=["status"])

    try:
        relative_path = build_report_file(report)
        report.file = relative_path
        report.status = "completed"
        report.completed_at = timezone.now()
        report.save(update_fields=["file", "status", "completed_at"])

        email = EmailMessage(
            subject="Your Carbon Grid report is ready",
            body="Your report has been generated successfully.",
            to=[report.email],
        )

        if report.file:
            email.attach_file(report.file.path)

        email.send()

        return {"report_id": report.id, "status": "completed"}

    except Exception:
        report.status = "failed"
        report.save(update_fields=["status"])
        raise