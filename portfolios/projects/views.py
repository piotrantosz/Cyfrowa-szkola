from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.utils.translation import ugettext as _

from .forms import ProjectForm
from .models import Project, User


def user_detail(request, user_id):
    queryset_list = Project.objects.filter(author=user_id)
    user = User.objects.get(id=user_id)
    context = {
        "object_list": queryset_list,
        "author": user,
    }
    return render(request, "user_detail.html", context)


def user_list(request):
    users = User.objects.all()
    for user in users:
        if not Project.objects.filter(author=user):
            users = users.exclude(username=user)  # Remove users without posts
    context = {
        "users": users,
    }
    return render(request, "user_list.html", context)


def project_list(request):
    queryset_list = Project.objects.all()
    context = {
        "object_list": queryset_list,
        "title": "Projects",
    }
    return render(request, "project_list.html", context)


def project_create(request):
    if not request.user.is_authenticated():
        raise Http404
    form = ProjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        messages.success(request, _("Successfully Created"))
        return HttpResponseRedirect(instance.get_absolute_url())
    elif form.errors:
        messages.error(request, _("Not Successfully Edited"))
    else:
        pass

    context = {
        "form": form,
    }
    return render(request, "project_form.html", context)


def project_detail(request, slug=None):
    instance = get_object_or_404(Project, slug=slug)
    context = {
        "title": instance.title,
        "instance": instance,
    }

    return render(request, "project_detail.html", context)


def project_update(request, slug=None):
    instance = get_object_or_404(Project, slug=slug)
    if not request.user.is_authenticated() or request.user != instance.author:
        raise Http404
    form = ProjectForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        messages.success(request, _("Successfully Edited"))
        return HttpResponseRedirect(instance.get_absolute_url())
    elif form.errors:
        messages.error(request, _("Not Successfully Edited"))
    else:
        pass

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "project_form.html", context)


def project_delete(request, slug=None):
    instance = get_object_or_404(Project, slug=slug)
    if not request.user.is_authenticated() or request.user != instance.author:
        raise Http404
    instance.delete()
    messages.success(request, _("Successfully Deleted"))
    return redirect("projects:list")
