from django.views.generic import base


class HomeView(base.TemplateView):
    template_name = "home.html"


class ProjectsView(base.TemplateView):
    template_name = "projects.html"

class CreditsView(base.TemplateView):
    template_name = "credits.html"

class FindMeOnlineView(base.TemplateView):
    template_name = "findmeonline.html"

class WorkExperienceView(base.TemplateView):
    template_name = "workexperience.html"