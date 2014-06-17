from django.db import models

from django.core.urlresolvers import reverse
# Create your models here.
class Contact(models.Model):

    first_name = models.CharField(max_length=255)

    last_name = models.CharField(
        max_length=255
    )

    email = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('contacts-view',kwargs={'pk':self.id})