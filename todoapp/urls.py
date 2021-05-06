from django.urls import path

from todoapp import views

app_name = "todo"
urlpatterns = [
    path('', views.TodoList.as_view(), name='todo-list'),
    path('item/<int:pk>/', views.TodoItemView.as_view(), name='todo-item'),
    path('item/<int:pk>/delete/', views.TodoItemDeleteView.as_view(), name='todo-item-delete'),
    path('item/<int:pk>/create/', views.TodoItemCreateView.as_view(), name='todo-item-create'),
    path('item/<int:pk>/update/', views.TodoItemUpdateView.as_view(), name='todo-item-update'),
]
