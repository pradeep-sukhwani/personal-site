from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.core.mail import send_mail
from core.managers.user_manager import UserManager, ResetPasswordManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('First Name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=30, blank=True)
    email = models.EmailField(_('Email Address'), unique=True)
    mobile = models.CharField(_('Mobile'), max_length=30, blank=True)
    created_on = models.DateTimeField(_('Created on'), auto_now_add=True, editable=True)
    is_active = models.BooleanField(_('Active'), default=True)
    # avatar = models.ForeignKey("core.Photo", null=True, blank=True)
    gallery = models.ManyToManyField("Photo", blank=True)
    is_staff = models.BooleanField(
        _('Staff Status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    # def get_avatar(self):
    #     if self.avatar:
    #         return self.avatar.pic.url

    def is_admin(self):
        if self.groups.filter(name="admin"):
            return True
        return False


class ResetPassword(models.Model):
    user = models.ForeignKey(User)
    key = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    objects = ResetPasswordManager()
