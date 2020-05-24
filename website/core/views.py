from django.views.generic import base


class HomeView(base.TemplateView):
    template_name = "home.html"


class ProjectsView(base.TemplateView):
    template_name = "projects.html"

class CreditsView(base.TemplateView):
    template_name = "credits.html"

class OnlineView(base.TemplateView):
    template_name = "online.html"

class EmploymentView(base.TemplateView):
    template_name = "employment.html"