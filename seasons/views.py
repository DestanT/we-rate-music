from django.shortcuts import render


def get_seasons_view(request):
    return render(request, "seasons/seasons_view.html")
