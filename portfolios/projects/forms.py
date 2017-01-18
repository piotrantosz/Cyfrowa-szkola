from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ('author',)
        fields = [
            "title",
            "category",
            "link",
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

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
