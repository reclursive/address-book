from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    big_fan = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Email(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="emails")
    email = models.EmailField()

    def __str__(self):
        return self.email