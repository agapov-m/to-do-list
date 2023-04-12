from django import template
from affairs.models import Category
from affairs.forms import AddCategory, AddTask
from datetime import date


register = template.Library()


@register.simple_tag()
def list_categories():
    return Category.objects.all()


@register.simple_tag()
def add_category():
    category_form = AddCategory()
    return category_form


@register.simple_tag()
def add_task():
    form = AddTask()
    return form


@register.simple_tag()
def get_current_date():
    current_date = date.today()
    return current_date
