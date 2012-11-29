from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response

from models import ApiKey, Thumbnail


def get_thumbnail(request):
    shot = None
    if 'url' in request.GET:
        url = request.GET['url']
        thumbnail, is_new = Thumbnail.objects.get_or_create(url=url)
        if not is_new:
            thumbnail.save()
        return HttpResponseRedirect(thumbnail.uri)
    return Http404('')
