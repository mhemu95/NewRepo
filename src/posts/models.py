from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_img = models.ImageField(default='default_image.jpg', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return self.title + ' | ' + str(self.pk)