from django.shortcuts import render, redirect
from .models import Problem, ProblemForm


def get_problem_from_id(id, index = 0): # Få problemet med den spesifike problemid'en
	return Problem.objects.filter(problem_id = id)[index]

def main_page(request):
	return render(request, "index.html", {"problems" : Problem.objects.all()})

def card_detail(request, problemId):
	return render(request, "card-detail.html", {"problem" : get_problem_from_id(problemId)})

def ticket_page(request, problemId):
	return render(request, "ticket.html", {"problem_id" : get_problem_from_id(problemId).problem_id})

def edit_problem_page(request, problemId):
	problem = Problem.objects.get(problem_id = problemId)
	return render(request, "edit/edit-problem.html", {"form" : ProblemForm(instance=problem), "problem_id" : problemId})

def edit_problem_backend(request, problemId):
	problem = Problem.objects.get(problem_id = problemId) # Få problemet med samme ID som den som skal endres
	if request.method == "POST": # Om brukeren sender data
		form = ProblemForm(request.POST, instance=problem) # Lag en ProblemForm instance av formen fra brukeren
		if form.is_valid(): # Valider formen
			form.save() # Endre problemet i databasen

			return redirect("/") # Send brukeren tilbake til hovedsiden

	return redirect("/") # ! Lag error side eller noe lignende