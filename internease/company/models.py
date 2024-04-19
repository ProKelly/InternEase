from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    description = models.TextField(max_length=500)
    photo = models.FileField(upload_to='company_photo/')
    address = models.CharField(max_length=100)
    website = models.URLField(max_length=200)
    location = models.CharField(max_length=1000, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Company"
    
    def __str__(self):
        return self.name + " | " + str(self.website) + " | " + str(self.location)
