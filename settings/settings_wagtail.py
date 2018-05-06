# Public
WAGTAIL_SITE_NAME = "This is yet another Wagtail Site or not?"


# Private
class MyWagtailConfig(object):
    INSTALLED_APPS = [
        'wagtail.contrib.forms',
        'wagtail.contrib.redirects',
        'wagtail.embeds',
        'wagtail.sites',
        'wagtail.users',
        'wagtail.snippets',
        'wagtail.documents',
        'wagtail.images',
        'wagtail.search',
        'wagtail.admin',
        'wagtail.core',

        'modelcluster',
        'taggit',
    ]

    MIDDLEWARE = [
        'wagtail.core.middleware.SiteMiddleware',
        'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    ]

    #WRONG WAY
    # @staticmethod
    # def STATICFILES_DIRS(BASE_DIR):
    #     import os
    #     return [
    #         # this is to include our own custom folder to the static directories
    #         os.path.join(BASE_DIR, "work_manager", "media")
    #     ]
