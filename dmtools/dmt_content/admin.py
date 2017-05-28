from django.contrib import admin
from dmt_content.models import Content


class ContentAdmin(admin.ModelAdmin):
    list_display = ('content_title', 'content_sponsor',)
    list_filter = ('content_title', 'content_sponsor',)
    search_fields = ('content_title', 'content_sponsor',)

    def add_view(self, request, form_url='', extra_context=None):
        self.exclude = ('content_folder', 'content_slug', 'content_used')
        return super(ContentAdmin, self).add_view(request)


admin.site.register(Content, ContentAdmin)
