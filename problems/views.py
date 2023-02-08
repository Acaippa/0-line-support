from django.shortcuts import render, redirect
from .models import Problem, ProblemForm, Kategori, UnderKategori, Ticket, TicketForm


def get_problem_from_id(id, index = 0): # Få problemet med den spesifike problemid'en
	return Problem.objects.filter(problem_id = id)[index]

def main_page(request):
	return render(request, "index.html", {"problems" : Problem.objects.all(), "categories" : Kategori.objects.all(), "subcategories" : UnderKategori.objects.all()})

def card_detail(request, problemId):
	return render(request, "card-detail.html", {"problem" : get_problem_from_id(problemId)})

def ticket_page(request, problemId):
	return render(request, "ticket.html", {"problem_id" : get_problem_from_id(problemId).problem_id, "ticket_form" : TicketForm()})


# ? Edit problem

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


# ? Add problem

def add_problem(request):
	problem_form = ProblemForm()
	return render(request, "add/add-problem.html", {"form" : problem_form})

def add_problem_backend(request):
	if request.method == "POST":
		form = ProblemForm(request.POST)
		if form.is_valid():
			form.save()

	return redirect("/")

# ? Delete problem

def delete_problem(request, problemId):
	instance = Problem.objects.get(problem_id = problemId)
	instance.delete()
	return redirect("/")

# ? Filter

def filter_backend(request):
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

	context = {"problems" : all_problems, "categories" : Kategori.objects.all(), "subcategories" : UnderKategori.objects.all(), "filters" : filters}

	return render(request, "index.html", context)

# ? Ticket

def ticket_backend(request):
	form = TicketForm(request.POST)
	if form.is_valid():
		form.save()
	return redirect("/")