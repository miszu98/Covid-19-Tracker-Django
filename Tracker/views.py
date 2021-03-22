from django.shortcuts import render
from . import covid_data



def index(request):
    data = covid_data.get_updated_data()
    return render(request, "index.html", {"data": data, "total": covid_data.get_total_cases()})
