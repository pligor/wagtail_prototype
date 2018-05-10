from django.contrib.auth.models import User
from django.conf import settings

class KeystoneUser(User):
    """ An unmanaged model to represent a Keystone user. This
    model is created by the KeystoneAuthentication provider and
    assigned to the request.user property """

    # these are populated by a call to Keystone
    uuid = None
    token = None
    roles = []

    class Meta:
        managed = False

    @property
    def sites(self):
        """ the list of sites that this user has access to """
        sites = []

        def check_valid_site_access(role_id, site_code):
            for r in self.roles:
                if r['role_category_id'] != role_id:
                    continue

                # check for a valid site_access for KSL in this role
                for s in r.get('organisation', {}).get('site_accesses', []):
                    if s.get('application', {}).get('code', '').lower() == site_code \
                            and s.get('level', '') in ['1', '2', '3', '4', '5']:
                        return True
            return False

        # check KSL
        if check_valid_site_access(1, settings.ARTICLE_SOURCE_CODE_KSL):
            sites.append(settings.ARTICLE_SOURCE_CODE_KSL)

        # check KSG
        if check_valid_site_access(2, settings.ARTICLE_SOURCE_CODE_KSG):
            sites.append(settings.ARTICLE_SOURCE_CODE_KSG)

        # check Groups if not already got access to KSL & KSG
        if settings.ARTICLE_SOURCE_CODE_KSL not in sites \
                and check_valid_site_access(3, settings.ARTICLE_SOURCE_CODE_KSL):
            sites.append(settings.ARTICLE_SOURCE_CODE_KSL)

        if settings.ARTICLE_SOURCE_CODE_KSG not in sites \
                and check_valid_site_access(3, settings.ARTICLE_SOURCE_CODE_KSG):
            sites.append(settings.ARTICLE_SOURCE_CODE_KSG)

        return sites
