#coding:utf-8
from django.http import HttpResponse, Http404
import datetime

from django.template.loader import get_template
from django.template import Context


def hello(request):
    return HttpResponse("ÖÐÎÄ".decode("gbk"))

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def current_datetime2(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date':now}))
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    assert False
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    html = "<html><body>In %s hour(s), it will be %s." % (offset, dt)
    return HttpResponse(html)

from django.shortcuts import render_to_response

def current_datetime3(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html',{'current_date':now})

# use locals()
def current_datetime4(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html',locals())

def display_meta(request):
    values = request.META.items()
    values.sort()
    html=[]
    for k,v in values:
        try:
            html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))
        except:
            pass
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
