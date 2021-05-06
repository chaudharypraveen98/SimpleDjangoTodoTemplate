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
