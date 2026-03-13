from django.urls import path
from .views import ingest_current_intensity, list_records

urlpatterns = [
    path("ingest/", ingest_current_intensity, name="ingest-current-intensity"),
    path("records/", list_records, name="list-records"),
]