from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class HttpRedirectMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if not request.META['HTTP_HOST'].startswith('www.'):
            return HttpResponseRedirect('https://www.sweetpotato.xyz')
    # def process_response(self, request, response):
    #     return response
