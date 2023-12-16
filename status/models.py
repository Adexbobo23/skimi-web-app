from django.db import models
from django.conf import settings
from django.utils import timezone

class StatusUpdate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='status_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        # Check if created_at is None (not set) and set it to current date and time
        if self.created_at is None:
            self.created_at = timezone.now()

        # Set expiration date to 24 hours from the creation time
        self.expiration_date = self.created_at + timezone.timedelta(hours=24)
        super().save(*args, **kwargs)
