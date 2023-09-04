from django.shortcuts import render


def get_profile_view(request):
    return render(request, "users/profile.html")
