from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.


def home(request):
    base = Todo.objects.all()
    form = TodoForm()
    context = {'base': base, 'form': form}
    return render(request, 'index.html', context)


def addTodo(request):
    new_todo = Todo(text=request.POST['text'])
    new_todo.save()
    return redirect('home')


def complete(request, todo_id):
    comp = Todo.objects.get(pk=todo_id)
    if comp.complete == True:
        comp.complete = False
    else:
        comp.complete = True
    comp.save()
    return redirect('home')


def deleteCompleted(request):
    delcomp = Todo.objects.filter(complete__exact=True).delete()
    return redirect('home')


def deleteAll(request):
    delAll = Todo.objects.all().delete()
    return redirect('home')
