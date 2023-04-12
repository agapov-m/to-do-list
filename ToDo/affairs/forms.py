from django import forms
from .models import Tasks, Category


class AddTask(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'task-input', 'placeholder': 'Добавить задачу'}),
            'category': forms.Select(attrs={'class': 'category-input'})
        }
    
    def __init__(self, *args, **kwargs):
        super(AddTask, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выберите список'
        self.fields['category'].initial = Category.objects.get(pk=1)


class AddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Новый список'})
        }
