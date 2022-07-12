from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Item


# Home page that lists all ToDo items
def view_list(request):
    items = Item.objects.all()
    
    return render(request, 'todo/list.html', {'items': items})


# Detail page for an item
def item_show(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'todo/show.html')


# Form page to create a new item
@csrf_exempt
def new(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'todo/new.html', context)
    
    if request.method == 'POST':
        title = request.POST.get('title', 'Default Title')
        description = request.POST.get('description', 'No description')

        new_item = Item(title=title, description=description)
        new_item.save()
        return HttpResponseRedirect('/list/')


# Create a new List Item
def item_create():
    pass


def item_edit():
    pass


def item_update():
    pass


def item_destroy():
    pass
