from django.contrib import admin
from dmt_content.models import Content
from .custom_functions_content import content_setup, content_slug, content_change_assigned_site
from glob import glob


class ContentAdmin(admin.ModelAdmin):
    list_display = ('content_title', 'content_sponsor',)
    list_filter = ('content_title', 'content_sponsor',)
    search_fields = ('content_title', 'content_sponsor',)

    def save_model(self, request, obj, form, change):
        if 'content_zip_file' in request.POST:
            obj.content_slug = content_slug(request.POST)
            obj.content_folder = content_setup(request.POST)
            obj.content_used = "No"
        else:
            obj.content_zip_file = "NULL"
            obj.content_siteid = content_change_assigned_site(request.POST)

        obj.save()

    def add_view(self, request, form_url='', extra_context=None):
        self.exclude = ('content_folder', 'content_slug', 'content_used')
        return super(ContentAdmin, self).add_view(request)


admin.site.register(Content, ContentAdmin)
