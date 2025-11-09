def user_profile(request):
    """Context processor to add user profile to all templates"""
    context = {}
    if request.user.is_authenticated:
        if hasattr(request.user, 'profile'):
            context['user_profile'] = request.user.profile
        else:
            context['user_profile'] = None
    else:
        context['user_profile'] = None
    return context

