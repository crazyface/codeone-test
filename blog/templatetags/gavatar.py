import urllib, hashlib
from django import template




register = template.Library()

def gavatar(email):
    default = "http://failedmessiah.typepad.com/.a/6a00d83451b71f69e20154350b9fb2970c-800wi"
    size = 40
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
    return {'img_src': gravatar_url}

register.inclusion_tag('core/gavatar.html')(gavatar)