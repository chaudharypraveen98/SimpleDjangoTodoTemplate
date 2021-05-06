## Simple Django TODO
This webapp will manage your daily tasks.
We will implement simple CRUD operation.

#### Steps
* Fork this repository.
* Git clone your repo by `https://github.com/<your username>/SimpleDjangoTodoTemplate.git`
* Make sure your conda environment or python virtual environment is activated.
* Create your first app by `python manage.py startapp todoapp`
* Now head to settings in **SimpleDjangoTodoTemplate** and add **todoapp.apps.TodoappConfig** in INSTALLED_APPS.
* Add the following in models.py in todoapp
```
class TodoItem(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title
```
* Create urls.py in todoapp and paste the code
```

```
* Open urls.py in SimpleDjangoTodoTemplate Folder and paste the code
```
path('todo/', include('todoapp.urls'))
```
* Create Super User Or admin by `python manage.py createsuperuser`

* Register model in admin by writing the below code in admin.py in todoapp.
```
from todoapp.models import TodoItem

admin.site.register(TodoItem)
```
* Create table by `python manage.py makemigrations`

* Then migrate it `python manage.py migrate`
* Create view for todoapp in views.py in todoapp
```
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from todoapp.models import TodoItem


class TodoList(ListView):
    model = TodoItem
    template_name = 'todoapp/todoitem_list.html'
    context_object_name = "todoItems"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TodoItemView(DetailView):
    model = TodoItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TodoItemDeleteView(DeleteView):
    model = TodoItem
    success_url = reverse_lazy('todo:todo-list')


class TodoItemCreateView(CreateView):
    model = TodoItem
    fields = ['title', 'description']


class TodoItemUpdateView(UpdateView):
    model = TodoItem
    fields = ['title', 'description']
```
* We need some templates to display our contents. Create a **template** in todoapp then create a **todoapp** directory in templates. Within todo create a html5 file.

* Always remember to include `{% load static %}` in html pages to load all static files.

* Similarly for static file. Create a **static** file directory in todoapp then a **todoapp** directory within a static directory. Then create a styles.css file.

* Then create some url path to match the view by writing in urls.py that we had created in todoapp.


