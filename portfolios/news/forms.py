from django.forms import ModelForm
from django.utils.translation import ugettext as _

from .models import News


class NewsForm(ModelForm):
    class Meta():
        model = News
        exclude = ('author',)
        fields = [
            "title",
            "header_image",
            "content",
        ]
        labels = {
            'title': _('Title'),
            'header_image': _('Header image'),
            'content': _('Content'),
        }
