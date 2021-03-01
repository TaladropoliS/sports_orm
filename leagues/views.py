from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Max, Count, F

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")

def filtros(request):
	ligas_beisbol = League.objects.filter(name__contains='Baseball')
	ligas_mujeres = League.objects.filter(name__contains='Women')
	ligas_hockey = League.objects.filter(name__contains='Hockey')
	ligas_no_futbol = League.objects.exclude(name__contains='Football').exclude(name__contains='Soccer')
	ligas_conferencias = League.objects.filter(name__contains='Conference')
	ligas_atlanticas = League.objects.filter(name__contains='Atlantic')
	equipos_dallas = Team.objects.filter(location__contains='Dallas')
	equipos_raptors = Team.objects.filter(team_name__contains='Raptors')
	equipos_city = Team.objects.filter(location__contains='City')
	equipos_t = Team.objects.filter(team_name__istartswith='T')
	equipos_ordenados = Team.objects.all().order_by('location')
	equipos_inv = Team.objects.all().order_by('-team_name')
	jugadores_cooper = Player.objects.filter(last_name__contains='Cooper')
	jugadores_joshua = Player.objects.filter(first_name__contains='Joshua')
	jugadores_joshua_cooper = Player.objects.filter(last_name__iexact='cooper').exclude(first_name__iexact='Joshua')
	jugadores_aow = Player.objects.filter(first_name__iexact='Alexander')|Player.objects.filter(first_name__iexact='Wyatt')

	context={
		"ligas_deisbol": ligas_beisbol,
		"ligas_mujeres":ligas_mujeres,
		"ligas_hockey": ligas_hockey,
		"ligas_no_futbol": ligas_no_futbol,
		"ligas_conferencias": ligas_conferencias,
		"ligas_atlanticas": ligas_atlanticas,
		"equipos_dallas": equipos_dallas,
		"equipos_raptors": equipos_raptors,
		"equipos_city": equipos_city,
		"equipos_t": equipos_t,
		"equipos_ordenados": equipos_ordenados,
		"equipos_inv": equipos_inv,
		"jugadores_cooper": jugadores_cooper,
		"jugadores_joshua": jugadores_joshua,
		"jugadores_joshua_cooper": jugadores_joshua_cooper,
		"jugadores_aow": jugadores_aow
	}
	return render(request, "leagues/filtros.html", context)

def filtros2(request):
	ligas_asc = League.objects.filter(name__iexact='Atlantic Soccer Conference')
	equipos_asc = Team.objects.filter(league__in=ligas_asc)

	boston_pinguins = Team.objects.filter(Q(team_name__icontains="penguins") & Q(location__icontains="boston"))
	jugadores_bp = Player.objects.filter(Q(curr_team__team_name__icontains="penguins") & Q(curr_team__location__icontains="boston"))

	jugadores_icbc = Player.objects.filter(curr_team__league__name__icontains="International Collegiate Baseball Conference")

	jugadores_cafa = Player.objects.filter(Q(curr_team__league__name__icontains="American Conference of Amateur Football") & Q(
        last_name__icontains="lopez"))

	jugadores_futbol = Player.objects.filter(curr_team__league__sport__icontains="Football")

	jugadores_sophia = Player.objects.filter(first_name__icontains="sophia")

	context={
		"equipos_asc": equipos_asc,
		"ligas_asc": ligas_asc,

		'jugadores_bp': jugadores_bp,
		'boston_pinguins': boston_pinguins,

		'jugadores_icbc': jugadores_icbc,

		'jugadores_cafa': jugadores_cafa,

		'jugadores_futbol': jugadores_futbol,

		'jugadores_sophia': jugadores_sophia,
	}
	return render(request, "leagues/filtros2.html", context)


























