from django import forms
from django.forms import ModelForm
from captcha.fields import ReCaptchaField
from django.core.exceptions import ValidationError

from .models import Project, User


class ProjectForm(ModelForm):
    captcha = ReCaptchaField(attrs={
        'theme': 'clean',
    })
    class Meta:
        model = Project
        exclude = ('author',)
        fields = [
            "title",
            "category",
            "content",
            "header_image",
        ]