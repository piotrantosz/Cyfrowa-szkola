from django.shortcuts import get_object_or_404, redirect, render, HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import News
from .forms import NewsForm
from django.utils.translation import ugettext as _

def news_list(request):
    queryset_list = News.objects.all()
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
        "title": "News",
        "page_request_var": page_request_var
    }
    return render(request, "news_list.html", context)


def news_detail(request, id=None):
    instance = get_object_or_404(News, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }

    return render(request, "news_detail.html", context)


def news_create(request):
    if not request.user.is_authenticated() or not request.user.is_staff:
        raise Http404
    form = NewsForm(request.POST or None, request.FILES or None, label_suffix = "")
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        messages.success(request, _("Successfully Created"))
        return HttpResponseRedirect(instance.get_absolute_url())
    elif form.errors:
        messages.error(request, _("Not Successfully Created"))
    else:
        pass

    context = {
        "form": form,
    }
    return render(request, "news_form.html", context)


def news_update(request, id=None):
    instance = get_object_or_404(News, id=id)
    if not request.user.is_authenticated() or request.user != instance.author:
        raise Http404
    form = NewsForm(request.POST or None, request.FILES or None, instance=instance, label_suffix="")
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
    return render(request, "news_form.html", context)


def news_delete(request, id=None):
    instance = get_object_or_404(News, id=id)
    if not request.user.is_authenticated() or request.user != instance.author:
        raise Http404
    instance.delete()
    messages.success(request, _("Successfully Deleted"))
    return redirect("news:list")