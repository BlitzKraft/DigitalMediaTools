from django.contrib import admin
from dmt_sponsors.models import Sponsor

nats_choices = ()

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('dmt_name', 'dmt_user', 'dmt_email', 'dmt_feature', 'dmt_status')
    list_filter = ('dmt_name', 'dmt_user', 'dmt_email', 'dmt_feature', 'dmt_status')
    search_fields = ('dmt_name', 'dmt_user', 'dmt_email', 'dmt_feature', 'dmt_status')

admin.site.register(Sponsor, SponsorAdmin)