"""
View configuration for home app
"""
from django.shortcuts import render
from django.contrib import messages

from django.shortcuts import redirect
from django.views.generic import TemplateView

from home.forms import ContactForm


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        kwargs['welcome_message'] = 'Welcome User!'
        return super().get_context_data(**kwargs)


    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))

class ContactView(TemplateView):
    template_name = 'home/contact.html'

    def get_context_data(self, **kwargs):
        kwargs['contact_form'] = ContactForm()
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))

class AboutView(TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))

class ResumeView(TemplateView):
    template_name = 'home/resume.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))

class UltimateView(TemplateView):
    template_name = 'home/ultimate.html'
