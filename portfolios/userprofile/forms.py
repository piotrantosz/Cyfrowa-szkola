from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "future_job", "avatar", "header_image", "short_description",
                  "long_description"]


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30,
                                 label=_('First name'),
                                 required=True,
                                 widget=forms.TextInput(
                                     attrs={'placeholder':
                                                _('First name')
                                            })
                                 )
    last_name = forms.CharField(max_length=30,
                                label=_('Last name'),
                                required=True,
                                widget=forms.TextInput(
                                    attrs={'placeholder':
                                               _('Last name')
                                           })
                                )

    future_job = forms.CharField(max_length=40,
                                 label=_('Future job'),
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