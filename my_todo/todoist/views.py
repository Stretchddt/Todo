from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def home(request):
    todos = Todo.objects.filter(author=request.user)

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form = TodoForm()

    context = {
        'todos': todos,
        'form': form
    }

    return render(request, 'todoist/home.html', context)

def update(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm(instance=todo)
    
    context = {
        'form': form
    }

    return render(request, 'todoist/update.html', context)

def delete(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        todo.delete()
        return redirect('home') 

    context = {
        'todo': todo
    }

    return render(request, 'todoist/delete.html', context)