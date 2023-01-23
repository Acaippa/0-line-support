from django.shortcuts import render
from .models import Problem

def split_capital(str): # Split stringen basert på store boksatver
	return_list = []
	temp_str = ""

	for index, letter in enumerate(str): # Loop gjennom alle bokstavene og legg de til temp_str. Om bokstaven er stor så legges temp_str in i return_list og temp_str tømmes
		if index == 0:
			temp_str += letter
		else:
			if letter.islower() == True:
				temp_str += letter
			else:
				return_list.append(temp_str)
				temp_str = ""
				temp_str += letter # Legg til den store bokstaven først i neste temp_str istedet for i slutten av forrige temp_str

	if len(temp_str) != 0:
		return_list.append(temp_str) # Sørg for at det ikke ligger igjen noe i temp_str når loopen er ferdig

	return return_list

def get_values_from_problem(problem):
	return[problem.__dict__[value] for value in problem.__dict__ if value[:1] != "_"]


def fields_to_dict(fields):
	return_dict = {}


	fields = str(fields)[1:-1].split(",")

	fields = [field[1:-1] for field in fields]

	for field in fields:
		field_key, field_value = field.split(":")

		key, value = field_value, field_key.split(".")[-1]

		return_dict[key] = split_capital(value)[0]

	
	return return_dict

def get_problem_from_id(id, index = 0): # Få problemet med den spesifike problemid'en
	return Problem.objects.filter(problem_id = id)[index]

def main_page(request):
	return render(request, "index.html", {"problems" : Problem.objects.all()})

def card_detail(request, problemId):
	return render(request, "card-detail.html", {"problem" : get_problem_from_id(problemId)})

def ticket_page(request, problemId):
	return render(request, "ticket.html", {"problem_id" : get_problem_from_id(problemId).problem_id})

def edit_problem_page(request, problemId):
	return render(request, "edit/edit-problem.html", {"problem" : get_values_from_problem(get_problem_from_id(problemId)), "problem_fields" : fields_to_dict(Problem._meta.get_fields())})