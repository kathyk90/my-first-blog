from django.contrib import admin

from .models import Choice, Question, Message, Q, Clas


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class ClasInline(admin.TabularInline):
    model = Clas
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['message_text']})]


class QAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['quantity']})]

    inlines = [ClasInline]
    

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Message, MessageAdmin)
admin.site.register(Q, QAdmin)  
                 
