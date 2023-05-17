from django import template


register = template.Library()

@register.filter(name='censor')
def censor(value, arg):
    bList = ['дур', 'коз']
    cEdit = value
    result = ''

    for w in bList:
        cTemp = cEdit.lower().replace(w, arg * len(w))
        cEdit = cTemp

    for i in range(0, len(value)):
        if (value[i] != cEdit[i]):
            result += cEdit[i].upper()
        else:
            result += cEdit[i]

    return result


@register.filter(name='is_filters_uses')
def is_filters_uses(value):
    filters_arg = value.find('&')
    if filters_arg != -1:
        is_first_list_now = value.find('?')
        if value[(is_first_list_now + 1): (is_first_list_now + 5)] == 'page':
            return value[filters_arg:]
        else:
            return ('&' + value[is_first_list_now + 1:])
    else:
        return ''

