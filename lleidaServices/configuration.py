#!/usr/bin/python

# Title           :lleidaClient.py
# Description     :This will create a header for a python script.
# Author          :Dhanasekara Pandian
# Email           :dhana.s@contecuae.com
# Date            :20191202
# Version         :0.1
# Usage           :python lleidaClient.py
# Notes           :This is proprietary software of i2i Telesource India Pvt Ltd.
# Python_version  :3.6

import os

from jinja2 import Environment, FileSystemLoader

dirname = os.path.dirname

TEMPLATES_PATH = os.path.join(dirname(__file__), os.path.join('templates'))


def _setup_jinja2():
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_PATH)
    )
    return env


def render_template(template_filename, **context):
    env = _setup_jinja2()
    template = env.get_template(template_filename)
    return template.render(context)
