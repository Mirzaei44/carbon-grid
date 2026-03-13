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
    
class Report(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]

    email = models.EmailField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    file = models.FileField(upload_to="reports/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.email} | {self.status}"