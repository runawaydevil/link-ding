from django.conf import settings

from bookmarks import utils
from bookmarks.models import Toast


def get_effective_theme(request):
    """Resolve effective theme: LD_THEME if set and valid, else map user profile (light→latte, dark→mocha, auto→auto)."""
    if settings.LD_THEME in ("latte", "frappe", "macchiato", "mocha", "auto"):
        return settings.LD_THEME
    profile_theme = getattr(request.user_profile, "theme", "auto")
    if profile_theme == "light":
        return "latte"
    if profile_theme == "dark":
        return "mocha"
    return "auto"


def effective_theme(request):
    """Context processor that exposes effective_theme for templates."""
    return {"effective_theme": get_effective_theme(request)}


def toasts(request):
    user = request.user
    toast_messages = (
        Toast.objects.filter(owner=user, acknowledged=False)
        if user.is_authenticated
        else []
    )
    has_toasts = len(toast_messages) > 0

    return {
        "has_toasts": has_toasts,
        "toast_messages": toast_messages,
    }


def app_version(request):
    return {"app_version": utils.app_version}
