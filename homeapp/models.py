from django.db import models
import re  # For extracting video ID

class Bird(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='birds/')
    description = models.TextField()
    youtube_url = models.CharField(max_length=255, blank=True, null=True)  # New field: Optional YouTube URL

    def __str__(self):
        return self.name

    def get_youtube_id(self):
        """
        Extracts the 11-character YouTube video ID from various URL formats.
        Returns None if no valid ID is found.
        """
        if not self.youtube_url:
            return None
        # Regex to match common YouTube URL patterns
        match = re.search(r'(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/ ]{11})', self.youtube_url)
        if match:
            return match.group(1)
        return None
