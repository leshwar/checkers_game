from django.template import Context, loader
from django.shortcuts import render, redirect
from django.views import View

class CheckerView(View):
    template_name = "checker.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})