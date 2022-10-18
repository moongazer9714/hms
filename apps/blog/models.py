from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title



class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title

def path_to_blog_image(instance,filename):
      title=instance.title
      category=instance.category
      return 'blog/{0}/{1}/images/{2}'.format(category, title, filename)

class Blog(models.Model):
      title = models.CharField(max_length=255)
      image = models.ImageField(upload_to=path_to_blog_image)
      content = RichTextField()
      category = models.ForeignKey(Category, on_delete=models.CASCADE)
      tag = models.ManyToManyField(Tag)
      created = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.title