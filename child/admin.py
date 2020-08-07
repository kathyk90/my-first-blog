from django.contrib import admin

from child.models import Choice, Questions


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Choice)
             
                 
