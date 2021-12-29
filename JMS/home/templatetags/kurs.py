from django import template

register = template.Library()

@register.filter
def exrate_display(value, choose):
  if choose == 'country':
    return value[0]
  elif choose == 'rate':
    rate = str(value[1])
    splitted = rate.split('.')[0]
    result = '{:,}'.format(int(splitted))
    return result