from django.contrib import admin
from .models import Content, Skill, Work, SubWork


class ContentsAdmin(admin.ModelAdmin):
    # 表示項目
    list_display = ["contents_type", "title", "sub_title", "date_created", "date_changed"]
    # 検索ボックス
    search_fields = ("title", "sub_title", "main_text")
    # フィルター
    list_filter = ['contents_type']


class SkillsAdmin(admin.ModelAdmin):
    # 表示項目
    list_display = ["content", "type", "name", "rank"]


admin.site.register(Content, ContentsAdmin)
admin.site.register(Skill, SkillsAdmin)
admin.site.register(Work)
admin.site.register(SubWork)
