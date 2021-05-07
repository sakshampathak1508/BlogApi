from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200,default="",blank=True)
    slug = models.SlugField(blank=True, null=True)
    author = models.CharField(max_length=200,default="",blank=True)
    description = models.TextField(default="",blank=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)
    image = models.ImageField(upload_to="blog/images",blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title.lower())

        super(Post, self).save(*args, **kwargs)