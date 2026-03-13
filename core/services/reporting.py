from pathlib import Path
from django.conf import settings
from django.utils import timezone

from core.models import CarbonRecord, Report


def build_report_file(report: Report):
    records = CarbonRecord.objects.select_related("region").all()[:100]

    reports_dir = Path(settings.MEDIA_ROOT) / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    filename = f"report_{report.id}.txt"
    file_path = reports_dir / filename

    lines = [
        "Carbon Grid Report",
        "==================",
        f"Generated at: {timezone.now()}",
        f"Total records: {CarbonRecord.objects.count()}",
        "",
    ]

    for record in records:
        lines.append(
            f"{record.region.name} | {record.from_time} | "
            f"forecast={record.forecast_intensity} | actual={record.actual_intensity}"
        )

    file_path.write_text("\n".join(lines), encoding="utf-8")
    return f"reports/{filename}"