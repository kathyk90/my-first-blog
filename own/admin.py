from django.contrib import admin

# Register your models here.

from own.models import Choice, Question_own


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class Question_ownAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question_own, Question_ownAdmin)
admin.site.register(Choice)
