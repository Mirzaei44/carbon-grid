from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class CarbonRecord(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="records")
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()
    forecast_intensity = models.IntegerField(null=True, blank=True)
    actual_intensity = models.IntegerField(null=True, blank=True)
    index_label = models.CharField(max_length=50, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-from_time"]

    def __str__(self):
        return f"{self.region.name} | {self.from_time}"