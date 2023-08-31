from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USER_TYPE_CHOICES = (
        ('vendor', 'Vendor'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='vendor')

    def __str__(self):
        return "{0}".format(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Product(models.Model):
    PENDING = 'pending'
    APPROVED = 'approved'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
    ]
    product_uuid = models.UUIDField(default=uuid.uuid4)
    vendor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return "{0}".format(self.product_name)

