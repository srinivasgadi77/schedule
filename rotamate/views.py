from django.shortcuts import redirect
from django.contrib import admin

def login_redirect(request):
    return redirect('/shiftrota/home')

def i18n_javascript(request):
  return admin.site.i18n_javascript(request)