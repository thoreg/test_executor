# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie

from test_executor.models import Run


@login_required
@ensure_csrf_cookie
def overview(request):
    context = RequestContext(request)
    return render_to_response('overview.html', context)


@login_required
def detail(request, run_id):
    context = RequestContext(request)
    try:
        context['run'] = Run.objects.get(id=run_id)
    except Run.DoesNotExist:
        pass

    return render_to_response('detail.html', context)
