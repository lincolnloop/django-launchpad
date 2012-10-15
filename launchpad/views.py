import datetime
from django.core.urlresolvers import reverse
from django import http
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, ProcessFormView

from jsonit.views import AJAXFormMixin

from . import forms, models, signals

class Signup(AJAXFormMixin, CreateView):
    """Signup form and Member creation"""
    form_class = forms.MemberForm
    template_name = 'launchpad/signup.html'

    def get_success_url(self):
        return reverse('launchpad_success')

    def form_valid(self, form):
        response = super(Signup, self).form_valid(form)
        signals.subscribed.send(sender=self.object)
        return response

class Success(TemplateView):
    """Signup success page"""
    template_name = 'launchpad/success.html'

class Unsubscribe(TemplateView, ProcessFormView):
    """Unsubscribe from list via signed key"""
    template_name = 'launchpad/unsubscribe.html'
    model = models.Member

    def get_member_for_key(self, key):
        try:
            return self.model.objects.get_by_unsubscribe_key(key)
        except self.model.DoesNotExist:
            raise http.Http404

    def get(self, request, *args, **kwargs):
        key = kwargs.pop('key')
        member = self.get_member_for_key(key)
        return self.render_to_response({'member': member})

    def post(self, request, *args, **kwargs):
        key = kwargs.pop('key')
        member = self.get_member_for_key(key)
        member.is_subscribed = False
        member.unsubscribe_time = datetime.datetime.now()
        member.save()
        signals.unsubscribed.send(sender=member)
        return self.render_to_response({'member': member})

