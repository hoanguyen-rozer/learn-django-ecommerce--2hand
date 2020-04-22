from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from django.db.models.signals import post_save, pre_save
# Create your models here.

from .signals import object_viewed_signal
from .utils import get_client_ip

User = settings.AUTH_USER_MODEL

class ObjectViewed(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    ip_address = models.CharField(max_length=220, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING) # User. Product, Order, Cart,...
    object_id = models.PositiveIntegerField() # user_id, product_id,...
    content_objects = GenericForeignKey('content_type', 'object_id') # Product Instance
    timestamp = models.DateTimeField(auto_now_add=True)
    #product = models.ForeignKey(Product) # id = 1, product_id.objectviewed_set.all()
    # order = models.ForeignKey(Order)
    #url 

    def __str__(self):
        return '%s viewed on %s' %(self.content_objects, self.timestamp) # most recent save show up first

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Object viewed'
        verbose_name_plural = 'Objects viewed'

def object_viewed_reciever(sender, instance, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender) #instance.__class__
    new_view_object = ObjectViewed.objects.create(
        user=request.user,
        content_type=c_type,
        object_id=instance.id, 
        ip_address=get_client_ip(request)
    )
    

object_viewed_signal.connect(object_viewed_reciever)
