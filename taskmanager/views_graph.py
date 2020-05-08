from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.dateformat import format
from django.db.models import Q, Count
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

import datetime
import json

from .forms import LoginForm, ProjectForm, CommentForm, ProjectForm, TaskForm
from .models import Project, Status, Comment, Task, Category, Subtask
from .models import Verb, Trace

def print_json(data):
    print(json.dumps(data, indent = 1))

@login_required(login_url = 'connect')
def graphs(request):
    return render(request, 'taskmanager/graphs/graphs.html', locals())


# ***************************************************************************
#  GANTT
# ***************************************************************************

@login_required(login_url = 'connect')
def gantt(request):
    # Juste pour envoyer une aggrégations de taches par projet a javascript ie :
    # tasks_by_project = list({
    #   project : nom_du_projet
    #   tasks : list({
    #       project_name : nom_du_projet_parent
    #       project_id : id_du_projet_parent
    #       name : nom_de_la_tache
    #       id_task : id_de_la_tache
    #       start : timestamp_unix_du_start_date_en_MILLISECONDES
    #       end : timestamp_unix_du_due_date_en_MILLISECONDES
    #   })
    #})
    current_user = User.objects.get(id = request.user.id)
    involved_projects = Project.objects.filter(members = current_user)
    tasks_by_project = []
    for project in involved_projects:
        tasks = Task.objects.filter(user = current_user, project = project).order_by('start_date')
        tasks_list = [dict(
            project_name = task.project.name,
            project_id = task.project.id,
            name = task.name,
            id_task = task.id,
            start = int(format(task.start_date, 'U'))*1000,
            end = int(format(task.due_date, 'U'))*1000
            ) for task in tasks]

        tasks_by_project_data = dict(project = project.name , tasks = tasks_list)
        tasks_by_project.append(tasks_by_project_data)

    tasks_by_project = json.dumps(tasks_by_project)
    return render(request, 'taskmanager/graphs/gantt.html', locals())


# ***************************************************************************
#  DIAGRAMME D'ACTIVITE
# ***************************************************************************

@login_required(login_url = 'connect')
def activitydiag(request):
    return render(request, 'taskmanager/graphs/activitydiag.html', locals())


# ***************************************************************************
#  BURNDOWN CHART
# ***************************************************************************

@login_required(login_url = 'connect')
def burndown(request):
    return render(request, 'taskmanager/graphs/burndown.html', locals())


# ***************************************************************************
#  RADAR TASK
# ***************************************************************************

@login_required(login_url = 'connect')
def radartask(request):
    current_user = User.objects.get(id = request.user.id)
    involved_projects = Project.objects.filter(members = current_user)

    info_project = []

    for project in involved_projects:
        members = project.members.all()
        member_data = []
        for member in members:
            count_task = Task.objects.filter(project = project).filter(user = member).count()
            member_data.append(dict(name = member.username, count = count_task))
        info_project.append(dict(
            name = project.name,
            id = project.id,
            members = member_data
        ))

    info_project = json.dumps(info_project)
    return render(request, 'taskmanager/graphs/radartask.html', locals())


# ***************************************************************************
#  RADAR ACTIVITY
# ***************************************************************************

@login_required(login_url = 'connect')
def radaractivity(request):


    if(request.POST.get('range') and request.POST.get('range') == "global"):
        involved_projects = Project.objects.filter(members = request.user)

        traces_sent = []
        for project in involved_projects:
            traces_sent.append(dict(
                axis = project.name,
                count = Trace.objects.filter(actor = request.user, object_project = project).count()
            ))

        return JsonResponse(traces_sent, safe = False, status=200)

    elif(request.POST.get('range') and request.POST.get('range') == "project"):
        print("Hello")

        return JsonResponse({'status' : "ok"}, status=200)

    return render(request, 'taskmanager/graphs/radaractivity.html', locals())


# ***************************************************************************
#  MANAGE APPLICATION
# ***************************************************************************
@login_required(login_url = 'connect')
def manageapp(request):
    if not request.user.is_superuser:
        return HttpResponse("Vous n'êtes pas autorisé.")
    all_traces = Trace.objects.all()
    return render(request, 'taskmanager/graphs/manageapp.html', locals())
