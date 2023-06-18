from .models import About, Skills, PersonalProjects, RecentWork, Tool
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render
# Create your views here.


class HomeTemplateView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['skills'] = Skills.objects.all()
        context['works'] = RecentWork.objects.all()
        context['tools'] = Tool.objects.all()
        return context


def personal_projects(request):
    personal = get_object_or_404(PersonalProjects)
    return render(request, "projects/projects.html", {"personal": personal})
