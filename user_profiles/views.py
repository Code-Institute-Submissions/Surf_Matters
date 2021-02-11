from django.shortcuts import render


def user_profile(request):
    """
    Display the user's profile
    """
    template = 'user_profiles/user_profile.html'
    context = {}

    return render(request, template, context)