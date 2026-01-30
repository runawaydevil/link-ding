from django.conf import settings
from django.http import JsonResponse

from bookmarks.context_processors import get_effective_theme

# Catppuccin theme_color (Mauve) and background_color per flavor
THEME_COLORS = {
    "latte": {"theme_color": "#8839ef", "background_color": "#eff1f5"},
    "frappe": {"theme_color": "#ca9ee6", "background_color": "#303446"},
    "macchiato": {"theme_color": "#c6a0f6", "background_color": "#24273a"},
    "mocha": {"theme_color": "#cba6f7", "background_color": "#1e1e2e"},
    "auto": {"theme_color": "#8839ef", "background_color": "#eff1f5"},
}


def manifest(request):
    effective = get_effective_theme(request)
    colors = THEME_COLORS.get(effective, THEME_COLORS["auto"])
    response = {
        "short_name": "links expert",
        "name": "links expert",
        "description": "Self-hosted bookmark service",
        "start_url": "bookmarks",
        "display": "standalone",
        "scope": "/" + settings.LD_CONTEXT_PATH,
        "theme_color": colors["theme_color"],
        "background_color": colors["background_color"],
        "icons": [
            {
                "src": "/" + settings.LD_CONTEXT_PATH + "static/logo.svg",
                "type": "image/svg+xml",
                "sizes": "512x512",
                "purpose": "any",
            },
            {
                "src": "/" + settings.LD_CONTEXT_PATH + "static/logo-512.png",
                "type": "image/png",
                "sizes": "512x512",
                "purpose": "any",
            },
            {
                "src": "/" + settings.LD_CONTEXT_PATH + "static/logo-192.png",
                "type": "image/png",
                "sizes": "192x192",
                "purpose": "any",
            },
            {
                "src": "/" + settings.LD_CONTEXT_PATH + "static/maskable-logo.svg",
                "type": "image/svg+xml",
                "sizes": "512x512",
                "purpose": "maskable",
            },
            {
                "src": "/" + settings.LD_CONTEXT_PATH + "static/maskable-logo-512.png",
                "type": "image/png",
                "sizes": "512x512",
                "purpose": "maskable",
            },
            {
                "src": "/" + settings.LD_CONTEXT_PATH + "static/maskable-logo-192.png",
                "type": "image/png",
                "sizes": "192x192",
                "purpose": "maskable",
            },
        ],
        "shortcuts": [
            {
                "name": "Add bookmark",
                "url": "/" + settings.LD_CONTEXT_PATH + "bookmarks/new",
            },
            {
                "name": "Archived",
                "url": "/" + settings.LD_CONTEXT_PATH + "bookmarks/archived",
            },
            {
                "name": "Unread",
                "url": "/" + settings.LD_CONTEXT_PATH + "bookmarks?unread=yes",
            },
            {
                "name": "Untagged",
                "url": "/" + settings.LD_CONTEXT_PATH + "bookmarks?q=!untagged",
            },
            {
                "name": "Shared",
                "url": "/" + settings.LD_CONTEXT_PATH + "bookmarks/shared",
            },
        ],
        "screenshots": [
            {
                "src": "/"
                + settings.LD_CONTEXT_PATH
                + "static/linkding-screenshot.png",
                "type": "image/png",
                "sizes": "2158x1160",
                "form_factor": "wide",
            }
        ],
        "share_target": {
            "action": "/" + settings.LD_CONTEXT_PATH + "bookmarks/new",
            "method": "GET",
            "enctype": "application/x-www-form-urlencoded",
            "params": {
                "url": "url",
                "text": "url",
                "title": "title",
            },
        },
    }

    return JsonResponse(response, status=200)
