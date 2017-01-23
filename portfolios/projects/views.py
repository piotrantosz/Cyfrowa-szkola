from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    users_list = User.objects.all()
    for user in users_list:
        if not Project.objects.filter(author=user):
            users_list = users_list.exclude(username=user)  # Remove users without posts
    paginator = Paginator(users_list, 30)  # Show 30 users on page
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        users = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        users = paginator.page(paginator.num_pages)

    context = {
        "users": users,
    }
    return render(request, "user_list.html", context)


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