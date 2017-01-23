from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.utils.translation import ugettext as _
from projects.models import Project

from .forms import ProfileForm

def profile_detail(request):
    if not request.user.is_authenticated():
        raise Http404
    User = get_user_model()
    user_query = User.objects.filter(username=request.user)
    for u in user_query:
        has_projects = False
        if Project.objects.filter(author=u):
            has_projects = True

        user = u


    context = {
        "user": user,
        "has_projects": has_projects,
    }

    return render(request, "profile.html", context)


def profile_update(request):
    if not request.user.is_authenticated():
        raise Http404
    User = get_user_model()
    user_query = User.objects.filter(username=request.user)

    for u in user_query:
        user = u

    form = ProfileForm(request.POST or None, request.FILES or None, instance=user)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        messages.success(request, _("Successfully Edited"))
        return redirect(request.META['HTTP_REFERER'])
    elif form.errors:
        messages.error(request, _("Not Successfully Edited"))
    else:
        pass

    context = {
        "instance": user,
        "form": form,
    }

    return render(request, "profile_form.html", context)