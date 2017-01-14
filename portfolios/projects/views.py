from django.shortcuts import get_object_or_404, redirect, render, HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ProjectForm
from .models import Project


def user_detail(request, user_id):
    queryset_list = Project.objects.filter(author=user_id)
    paginator = Paginator(queryset_list, 30)  # Show 30 contacts per page, even number (design)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset_list = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset_list,
        "title": "List",
        "page_request_var": page_request_var
    }
    return render(request, "project_list.html", context)


def project_list(request):
    queryset_list = Project.objects.all()
    paginator = Paginator(queryset_list, 30)  # Show 30 contacts per page, even number (design)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset_list = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset_list,
        "title": "Projects",
        "page_request_var": page_request_var
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
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    elif form.errors:
        messages.error(request, "Not Successfully Edited")
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
        messages.success(request, "Successfully Edited")
        return HttpResponseRedirect(instance.get_absolute_url())
    elif form.errors:
        messages.error(request, "Not Successfully Edited")
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
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("projects:list")
