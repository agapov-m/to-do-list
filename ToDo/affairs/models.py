from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Мои задачи')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('get_category', kwargs = {'item_id': self.id}) 
        

class Tasks(models.Model):
    title = models.CharField(max_length=150, verbose_name='Текущие задачи')
    date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default = False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Мои задачи', null=True, related_name = 'get_tasks')

    class Meta:
        verbose_name = 'Текущая задача'
        verbose_name_plural = 'Текущие задачи'

    def __str__(self):
        return self.title