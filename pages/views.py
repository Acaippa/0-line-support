from django.shortcuts import render
from .models import Problem

# Create your views here.
def main_page(request):
	return render(request, "index.html", {"problems" : Problem.objects.all()})

def card_detail(request, problemId):
	return render(request, "card-detail.html", {"problem" : Problem.objects.filter(problem_id = problemId)[0]})

def ticket_page(request, problemId):
	return render(request, "ticket.html", {"problem_id" : Problem.objects.filter(problem_id = problemId)[0].problem_id})