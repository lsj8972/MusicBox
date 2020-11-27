from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from music.models import Music, Artist, Entertainment

#--- TemplateView
class MusicModelView(TemplateView):
    template_name = 'music/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['model_list'] = ['Music', 'Artist', 'Entertainment']
        return context

#--- ListView
class MusicList(ListView):
    model = Music

class ArtistList(ListView):
    model = Artist

class EntertainmentList(ListView):
    model = Entertainment

#--- DetailView
class MusicDetail(DetailView):
    model = Music

class ArtistDetail(DetailView):
    model = Artist

class EntertainmentDetail(DetailView):
    model = Entertainment