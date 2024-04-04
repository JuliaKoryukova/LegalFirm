from django.db import models

class LegalFirmManager(models.Manager):
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)

class LegalFirm(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    objects = LegalFirmManager()

    class Meta:
        db_table = 'legal_firm'

class Service(models.Model):
    firm = models.ForeignKey(LegalFirm, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

class Contact(models.Model):
    firm = models.OneToOneField(LegalFirm, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
