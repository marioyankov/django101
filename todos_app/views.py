from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from todos_app.forms import TodoForm
from todos_app.models import Todo


def index(request, form=None):
    if not form:
        form = TodoForm()

    context = {
        'todos': Todo.objects.all(),
        'todo_form': form,
    }

    return render(request, 'todos_app/index.html', context)

@require_POST
def create_todo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        todo = Todo(**form.cleaned_data, is_done=False)
        todo.save()
        return redirect('todos index')

    return index(request, form)