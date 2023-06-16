from .models import About, Skills, PersonalProjects, RecentWork
from django.views.generic import TemplateView
# Create your views here.


class HomeTemplateView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['skills'] = Skills.objects.all()
        context['works'] = RecentWork.objects.all()
        context['personalprojects'] = PersonalProjects.objects.all()
        return context
