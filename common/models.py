from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MediaFile(BaseModel):
    file = models.FileField(upload_to='files')

    def __str__(self):
        return self.file.name
    


class BlogPost(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    content = models.TextField()
    image = models.ForeignKey(MediaFile, on_delete=models.SET_NULL, null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)
    comment_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title