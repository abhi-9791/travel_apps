from django.db import models

class Destination(models.Model):
    CATEGORY_CHOICES = [
        ('Beach', 'Beach'),
        ('Mountain', 'Mountain'),
        ('City', 'City'),
        ('Historical', 'Historical'),
    ]

    name = models.CharField(max_length=256)
    country = models.CharField(max_length=100)
    description = models.TextField()
    best_time_to_visit = models.CharField(max_length=256)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
