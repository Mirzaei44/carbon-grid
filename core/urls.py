from django.urls import path
from .views import ingest_current_intensity, list_records, dashboard_summary, generate_report, dashboard_page

urlpatterns = [
    path("ingest/", ingest_current_intensity, name="ingest-current-intensity"),
    path("records/", list_records, name="list-records"),
    path("dashboard-summary/", dashboard_summary, name="dashboard-summary"),
    path("reports/generate/", generate_report, name="generate-report"),
    path("dashboard/", dashboard_page, name="dashboard-page"),
]