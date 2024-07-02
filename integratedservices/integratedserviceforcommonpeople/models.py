# models.py
from django.db import models

SERVICE_TYPES = [
    ('hospitals', 'Hospitals'),
    ('cab', 'Cab'),
    ('government', 'Government'),
    ('tourism', 'Tourism'),
]

class Service(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    whatsapp_number = models.CharField(max_length=15)
    website = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name