from django.http import HttpResponse
from django.urls import reverse

from bookmarks.models import GlobalSettings

# Use 302 (temporary) so redirect is not cached; relative path avoids host/port confusion in Docker
REDIRECT_STATUS = 302


def _redirect_response(url, status=REDIRECT_STATUS):
    """Build a 302 redirect manually so uWSGI does not alter status or Location."""
    response = HttpResponse(status=status)
    response.status_code = 302
    response["Location"] = url
    response["Content-Length"] = "0"
    return response


def root(request):
    # Redirect unauthenticated users to the configured landing page
    if not request.user.is_authenticated:
        global_settings = request.global_settings

        if global_settings.landing_page == GlobalSettings.LANDING_PAGE_SHARED_BOOKMARKS:
            return _redirect_response(reverse("linkding:bookmarks.shared"))
        return _redirect_response(reverse("login"))

    # Redirect authenticated users to the bookmarks page
    return _redirect_response(reverse("linkding:bookmarks.index"))
