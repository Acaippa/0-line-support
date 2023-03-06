from django.shortcuts import render, redirect
from .models import Problem, Kategori, UnderKategori
from .forms import ProblemForm, TicketForm


def get_problem_from_id(id, index = 0): # Få problemet med den spesifike problemid'en
	return Problem.objects.filter(problem_id = id)[index]


def home(request):
	all_problems = Problem.objects.all()

	if request.method == "POST":
		filters = request.POST

		filters_temp = filters.dict()
		filters_temp["csrfmiddlewaretoken"] = 0

		filters = filters_temp

		all_problems = Problem.objects.all()
		if "category-filter" in filters:
			all_problems = all_problems.filter(kategori__navn = filters["category-filter"])

		if "subcategory-filter" in filters:
			all_problems = all_problems.filter(under_kategori__navn = filters["subcategory-filter"])

		if "filter-text" in filters:
			all_problems = all_problems.filter(tittel__icontains = filters["filter-text"])

	return render(request, "index.html", {"problems" : all_problems, "categories" : Kategori.objects.all(), "subcategories" : UnderKategori.objects.all()})


def card_detail(request, problemId):
	problem = get_problem_from_id(problemId)
	return render(request, "card-detail.html", {"problem" : problem})


def ticket(request):
	ticket_form = TicketForm()

	if request.method == "POST":
		ticket_form = TicketForm(request.POST)
		"""
		TicketForm objektet sjekker om formen er valid, om den ikke er valid legger den til elementer med error meldinger. Denne nye formen blir da vist til brukeren slik at hen får greie på hva som må endres for at ticketen kan legges til.
		"""
		if ticket_form.is_valid():
			ticket_form.save()
			return redirect("/")
	
	return render(request, "ticket.html", {"ticket_form" : ticket_form})



# ? Edit problem

def edit_problem(request, problemId):
	problem = Problem.objects.get(problem_id = problemId)
	problem_form = ProblemForm(instance=problem)

	if request.method == "POST": # Om brukeren sender data
		problem_form = ProblemForm(request.POST, instance=problem) # Lag en ProblemForm instance av formen fra brukeren
		if problem_form.is_valid(): # Valider formen
			problem_form.save() # Endre problemet i databasen

			return redirect("/") # Send brukeren tilbake til hovedsiden

	return render(request, "edit-problem.html", {"form" : problem_form, "problem_id" : problemId})



# ? Add problem

def add_problem(request):
	problem_form = ProblemForm()

	if request.method == "POST":
		problem_form = ProblemForm(request.POST)
		if problem_form.is_valid():
			problem_form.save()

			return redirect("/")

	return render(request, "add-problem.html", {"form" : problem_form})
	


# ? Delete problem

def delete_problem(request, problemId):
	instance = Problem.objects.get(problem_id = problemId)
	instance.delete()
	return redirect("/")