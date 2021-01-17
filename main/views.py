from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import TemplateDoesNotExist
from django.template.loader import get_template


class IndexView(TemplateView):
    template_name = 'main/index.html'


def other_page(request, page):
    try:
        template = get_template(f'main/{page}.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))
