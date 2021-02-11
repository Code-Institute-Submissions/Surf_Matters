from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm


def user_profile(request):
    """
    Display the user's profile
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    template = 'user_profiles/user_profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)
