from django import template

register = template.Library()

@register.simple_tag
def idx(list_, index):
  try:
    res = list_[int(index)]
  except:
    res = ""
  return res
