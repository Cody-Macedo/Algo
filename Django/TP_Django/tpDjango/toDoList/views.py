from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from .forms import TaskForm
from .models import Task


# Create your views here.
def test(request):
    template = loader.get_template('to_do_list.html')
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    try:
        tasks = Task.objects.all()
    except Task.DoesNotExist:
        raise Http404("Question does not exist")
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/todolist/')
    # else:
    form = TaskForm()
    context = {'form': form, 'tasks': tasks}
    return render(request, 'to_do_list.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    print("***task: ", task.__str__())
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/to_do_list/')

    form = TaskForm(instance=task)
    context = {'form': form}
    return render(request, 'update_task.html', context)
