from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import OrderBy


class InternApplication(models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    school = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    support_leter = models.FileField(upload_to='support_leter')
    photo =  models.FileField(upload_to='photo')
    is_registered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Applications"
    
    def __str__(self):
        return self.name + " | " + self.tel

amounts = (('10000frs','10000frs'), ('20000frs', '20000frs'),)

class InternRegistration(models.Model):
    intern_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    account = models.OneToOneField(InternApplication, on_delete=models.CASCADE, related_name='application')
    momo_number = models.CharField(max_length=20)
    amount = models.CharField(max_length=100, choices=amounts)
    created = models.DateTimeField(auto_now_add=True)
    has_paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Registered Interns"
    
    def __str__(self):
        return self.intern_id + "-" + self.name


