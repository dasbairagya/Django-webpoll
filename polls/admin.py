from django.contrib import admin
from .models import Question
from .models import Choice

# pass admin.StackedInline or admin.TabularInline to look at the options on a single page
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# Customize Question Admin
class QuestionAdmin(admin.ModelAdmin):
    '''When the admin displays the question page, it shows only the question text field.
    You can customize the model class definition to display a list of fields using list_display.
    The model class fields or any functions defined within the model can be used as elements to
    display on the list.
    '''
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        ('Question', {'fields': ['question_text']}),
        ('Date info', {'fields': ['pub_date'], 'classes': ['collapse']}), # Collapse the date info section
    ]
    inlines = [ChoiceInline] # Add choices to the same questions

# Register your models here.
# admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


