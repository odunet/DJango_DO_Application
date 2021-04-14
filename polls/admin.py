from django.contrib import admin

# Register your models here.
from .models import Choice, Questions

# admin.site.register(Questions)
# admin.site.register(Choice)

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]

admin.site.register(Questions, QuestionsAdmin)