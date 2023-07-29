from django.db import models
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.dispatch import receiver


class Tags(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "tags"
    
    def __str__(self):
        return self.name


@receiver(post_save, sender=Tags)
def my_signal_fn(sender, instance, **kwargs):
    print("sender", sender)
    print("instance", instance)
    print("signal called after save")


@receiver(pre_delete, sender=Tags)
def my_signal_fn_2(sender, instance, **kwargs):
    print("signal called before delete")
    

@receiver(post_delete, sender=Tags)
def my_signal_fn_3(sender, instance, **kwargs):
    print("signal called after delete")


@receiver(post_delete, sender=Tags)
def my_signal_fn_3(sender, instance, **kwargs):
    print("signal called after delete")
