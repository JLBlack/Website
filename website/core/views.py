from django.views.generic import base


class HomeView(base.TemplateView):
    template_name = "home.html"
