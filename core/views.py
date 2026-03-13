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
    queryset = CarbonRecord.objects.select_related("region").all()[:100]
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
