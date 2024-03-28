from rest_framework.throttling import UserRateThrottle

"""
        restrictions unneccesary accesing
"""
class Check_unneccessary_accesing(UserRateThrottle):
    scope = 'users'
    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            ident = request.user.username
        else:
            ident = self.get_ident(request) 
        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }