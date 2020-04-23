from django.contrib import admin
from django.contrib.admin import TabularInline


from omniport.admin.site import omnipotence
from formula_one.admin.model_admins.base import ModelAdmin
from no_dues.models import (
    Authority, Verifier, Permission, Subscriber
)


class PermissionInline(TabularInline):
    """"
    This class implements Permission inline for the Subscriber
    """

    model = Permission
    fk_name = 'subscriber'


@admin.register(Subscriber, site=omnipotence)
class SubscriberAdmin(ModelAdmin):
    """
    The class controls the behaviour of Subscriber in Omnipotence
    """

    inlines = (PermissionInline, )


omnipotence.register(Authority)
omnipotence.register(Verifier)
omnipotence.register(Permission)
