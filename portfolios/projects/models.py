from __future__ import unicode_literals

from django import forms
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator, UnicodeUsernameValidator
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.forms.extras import widgets
from django.utils import six, timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator() if six.PY3 else ASCIIUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'))
    avatar = models.ImageField(null=True, blank=True)
    header_image = models.ImageField(null=True, blank=True)
    short_description = models.TextField(max_length=200, null=True, blank=True)
    long_description = models.TextField(max_length=3000, null=True, blank=True)
    future_job = models.CharField(max_length=40)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['-date_joined']

    def clean(self):
        super(User, self).clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_user_url(self):
        return reverse("projects:user_detail", kwargs={"user_id": self.id})


class Project(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=30)
    content = models.TextField()
    header_image = models.ImageField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Project.objects.filter(slug=slug).order_by("-id")
    if qs.exists():
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_project_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_project_receiver, sender=Project)
