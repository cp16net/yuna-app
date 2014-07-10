from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
# from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import logout as auth_logout, login


def home(request):
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    return render_to_response('home.html',
                              context_instance=context)

@login_required
def login_redirect(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/%s' % request.user.username)
    return HttpResponseRedirect('/')