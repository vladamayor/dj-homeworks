from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator



def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    bus_stations = []
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for raw in reader:
            bus_station = {}
            bus_station['Name'] = raw['Name']
            bus_station['Street'] = raw['Street']
            bus_station['District'] = raw['District']
            bus_stations.append(bus_station)
    paginator = Paginator(bus_stations, 10)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    context ={
        'bus_stations': page,
        'page': page
    }

    return render(request, 'stations/index.html', context)
