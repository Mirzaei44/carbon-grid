from core.models import Region, CarbonRecord


def save_intensity_payload(payload):
    items = payload.get("data", [])

    saved = 0

    for item in items:
        intensity = item.get("intensity", {})

        region, _ = Region.objects.get_or_create(name="National Grid")

        CarbonRecord.objects.update_or_create(
            region=region,
            from_time=item["from"],
            to_time=item["to"],
            defaults={
                "forecast_intensity": intensity.get("forecast"),
                "actual_intensity": intensity.get("actual"),
                "index_label": intensity.get("index", ""),
            },
        )
        saved += 1

    return saved
