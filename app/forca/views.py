from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class Perfil (LoginRequiredMixin, TemplateView):
	template_name = 'perfil.html'


class Ranking (TemplateView):
	template_name = 'ranking.html'

class Jogo (TemplateView):
	template_name = 'jogo.html'

class Palavra (TemplateView):
	template_name = 'cadastroPalavra.html'	