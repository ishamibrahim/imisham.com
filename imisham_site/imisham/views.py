# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from imisham_site.settings import STATIC_URL


def index(request):
    template = loader.get_template("index.html")
    context = {
        "STATIC_URL": STATIC_URL
    }

    return HttpResponse(template.render(context, request))