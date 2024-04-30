from django.db import models
from django.urls import reverse

# Create your models here.
class NewPostModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    text = models.TextField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('new_detail', args=[str(self.pk)])