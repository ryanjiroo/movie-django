import json
from django.shortcuts import render
from django.http import Http404
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parent / 'movies.json'

def load_movies():
    with open(DATA_PATH) as file:
        return json.load(file)

def home(request):
    movies = load_movies()
    return render(request, 'index.html', {'movies': movies})

def movie_detail(request, id):
    movies = load_movies()
    movie = next((movie for movie in movies if movie['id'] == id), None)
    if not movie:
        raise Http404("Movie not found")
    return render(request, 'detail.html', {'movie': movie})