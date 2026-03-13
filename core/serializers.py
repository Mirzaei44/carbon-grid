from rest_framework import serializers
from .models import Region, CarbonRecord


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "name"]


class CarbonRecordSerializer(serializers.ModelSerializer):
    region = serializers.CharField()

    class Meta:
        model = CarbonRecord
        fields = [
            "region",
            "from_time",
            "to_time",
            "forecast_intensity",
            "actual_intensity",
            "index_label",
        ]


class ReportRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()