from django.contrib import admin

# Register your models here.
from .models import BillingProfile, Card

admin.site.register(BillingProfile)

admin.site.register(Card)