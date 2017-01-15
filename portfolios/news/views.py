from django.shortcuts import get_object_or_404, redirect, render, HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import News

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

