from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks, Category
from .forms import AddTask, AddCategory
from django.views.generic import CreateView


def index_page(request):
    tasks = dict()
    for category in Category.objects.all():
        tasks[category] = {'current': category.get_tasks.filter(completed=False),
                           'completed': category.get_tasks.filter(completed=True)}
    
    return render(request, 'affairs/index.html', {'tasks': tasks})


def get_category(request, item_id):
    tasks = Tasks.objects.filter(category_id=item_id, completed=False)
    completed = Tasks.objects.filter(category_id=item_id, completed=True)
    category = Category.objects.get(pk=item_id)
        
    return render(request, 'affairs/get_category.html', {'tasks': tasks, 'completed': completed, 'category': category})


class AddCategory(CreateView):
    form_class = AddCategory
    template_name = None
    context_object_name = 'category_form'


def add_task(request):
    curr_path = request.GET.get('url')
    if request.method == 'POST':
        form = AddTask(request.POST)
        category_id = request.POST.get('category_id')
        category = Category.objects.get(pk=category_id)

        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.category = category
            new_task.save()
            return redirect(curr_path)


def complete_task(request, task_id):
    curr_path = request.GET.get('url')
    if request.method == 'POST':
        task = Tasks.objects.get(pk=task_id)
        task.completed = abs(task.completed - 1)
        task.save()
        return redirect(curr_path)
    

def delete_task(request, task_id):
    curr_path = request.GET.get('url')
    task = get_object_or_404(Tasks, pk=task_id)
    task.delete()
    return redirect(curr_path)


def delete_category(request, category_id):
    task = get_object_or_404(Category, pk=category_id)
    task.delete()
    return redirect('home')

    