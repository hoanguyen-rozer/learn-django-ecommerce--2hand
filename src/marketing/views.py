from django.shortcuts import redirect, render
from django.views.generic import UpdateView
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
from .models import MarketingPreference
from .forms import MarketingPreferenceForm


class MarketingPreferenceUpdateView(SuccessMessageMixin, UpdateView):
    form_class = MarketingPreferenceForm
    template_name = 'base/forms.html'
    success_url = '/settings/email/'
    success_message = "Your email preferences have been updated! Thank you"

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if not user.is_authenticated:
            return redirect('/login/?next=/settings/email/')
        return super(MarketingPreferenceUpdateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Update Email Marketing'
        return context

    def get_object(self):
        user = self.request.user
        obj, created = MarketingPreference.objects.get_or_create(user=user)
        return obj
