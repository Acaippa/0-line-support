from django.shortcuts import render

# Create your views here.
def main_page(request):
	return render(request, "index.html")

def card_detail(request):
	return render(request, "card-detail.html")

def ticket_page(request):
	return render(request, "ticket.html")