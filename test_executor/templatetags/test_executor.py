# -*- coding: utf-8 -*-
from ansi2html import Ansi2HTMLConverter
from django import template

from test_executor.models import Status

register = template.Library()


@register.filter
def as_string(value):
    return Status.values[value]


@register.filter
def as_html(value):
    conv = Ansi2HTMLConverter()
    return conv.convert(value)
