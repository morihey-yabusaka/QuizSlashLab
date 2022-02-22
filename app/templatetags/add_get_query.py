from atexit import register
from django import template

register = template.Library()

@register.simple_tag
def get(request, **kwargs):
  updated = request.GET.copy()
  for k, v in kwargs.items():
    updated[k] = v

  return updated.urlencode()