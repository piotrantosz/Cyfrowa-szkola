from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from captcha.fields import ReCaptchaField
from django.core.exceptions import ValidationError

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


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30,
                                 label='First name',
                                 required=True,
                                 widget=forms.TextInput(
                                     attrs={'placeholder':
                                                _('First name')
                                            })
                                 )
    last_name = forms.CharField(max_length=30,
                                label='Last name',
                                required=True,
                                widget=forms.TextInput(
                                    attrs={'placeholder':
                                               _('Last name')
                                           })
                                )

    future_job = forms.CharField(max_length=40,
                                 required=True,
                                 widget=forms.TextInput(
                                     attrs={'placeholder':
                                                _('Who you want to be in future? (job)')
                                            })
                                 )

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.future_job = self.cleaned_data['future_job']
        user.save()
