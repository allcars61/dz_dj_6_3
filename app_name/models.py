from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('phone_detail', kwargs={'slug': self.slug})