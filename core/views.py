from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CarbonRecord
from .serializers import CarbonRecordSerializer
from .services.carbon_api import fetch_current_intensity
from .services.ingestion import save_intensity_payload


@api_view(["POST"])
def ingest_current_intensity(request):
    payload = fetch_current_intensity()
    saved = save_intensity_payload(payload)
    return Response({"status": "ok", "saved": saved})


@api_view(["GET"])
def list_records(request):
    queryset = CarbonRecord.objects.select_related("region").all()

    region = request.GET.get("region")
    date_from = request.GET.get("from")
    date_to = request.GET.get("to")

    if region:
        queryset = queryset.filter(region__name__icontains=region)

    if date_from:
        queryset = queryset.filter(from_time__date__gte=date_from)

    if date_to:
        queryset = queryset.filter(to_time__date__lte=date_to)

    queryset = queryset[:100]

    serializer = CarbonRecordSerializer(
        [
            {
                "region": obj.region.name,
                "from_time": obj.from_time,
                "to_time": obj.to_time,
                "forecast_intensity": obj.forecast_intensity,
                "actual_intensity": obj.actual_intensity,
                "index_label": obj.index_label,
            }
            for obj in queryset
        ],
        many=True,
    )
    return Response(serializer.data)


@api_view(["GET"])
def dashboard_summary(request):
    queryset = CarbonRecord.objects.select_related("region").all()

    total_records = queryset.count()
    latest_record = queryset.first()

    actual_values = [x.actual_intensity for x in queryset if x.actual_intensity is not None]
    forecast_values = [x.forecast_intensity for x in queryset if x.forecast_intensity is not None]

    avg_actual = round(sum(actual_values) / len(actual_values), 2) if actual_values else None
    avg_forecast = round(sum(forecast_values) / len(forecast_values), 2) if forecast_values else None

    return Response(
        {
            "total_records": total_records,
            "average_actual_intensity": avg_actual,
            "average_forecast_intensity": avg_forecast,
            "latest_region": latest_record.region.name if latest_record else None,
            "latest_from_time": latest_record.from_time if latest_record else None,
            "latest_actual_intensity": latest_record.actual_intensity if latest_record else None,
        }
    )