from captcha.fields import ReCaptchaField
from django.forms import ModelForm

from .models import Project


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
