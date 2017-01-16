from django.forms import ModelForm
from .models import News
from django.utils.translation import ugettext as _


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