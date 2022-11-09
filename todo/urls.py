from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.addTodo, name='add'),
    path('complete/<todo_id>', views.complete, name='complete'),
    path('deleteCompleted', views.deleteCompleted, name='delcomp'),
    path('deleteAll', views.deleteAll, name='delAll')
]
