from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    # # SELECT * FROM movies_movie
    # Movie.objects.filter(release_year=1984)
    # # SELECT * FROM movies_move WHERE ...
    # Movie.objects.get(id=1)

    # output = ', '.join([m.title for m in movies])
    # return HttpResponse(output)

    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    # try:
    #     movie = Movie.objects.get(id=movie_id)
    #     # return HttpResponse(movie)
    #     return render(request, 'movies/detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404()

    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
