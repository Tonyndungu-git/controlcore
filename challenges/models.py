from django.db import models


class Challenge(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    difficulty = models.CharField(max_length=50, choices=[('Advanced', 'Advanced')])
    video_url = models.URLField()
    github_url = models.URLField()
    tags = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='challenges/', blank=True)

    def __str__(self):
        return self.title
