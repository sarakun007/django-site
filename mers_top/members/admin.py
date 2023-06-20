from django.contrib import admin
from .models import Member, Pictures


class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "content", "joined_date", 'photo')
    search_fields = ('firstname', 'photo')
    list_filter = ('joined_date',)


class PictAdmin(admin.ModelAdmin):
    list_display = ('onlyphoto',)


admin.site.register(Member, MemberAdmin)
admin.site.register(Pictures, PictAdmin)
