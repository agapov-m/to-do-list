from django.contrib import admin

from .models import Tasks, Category

class CurrentTasksAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category', 'completed')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)

admin.site.register(Tasks, CurrentTasksAdmin)
admin.site.register(Category, CategoryAdmin)
