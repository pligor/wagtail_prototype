from django.views.generic import View  # TemplateView
from django.http import HttpResponse
from django.shortcuts import redirect


class CustomCBV(View):

    def dispatch(self, request, *args, **kwargs):
        dont_like_option = request.GET.get('dont_like')

        if dont_like_option is not None and dont_like_option.lower() == 'true':
            return redirect(to='tasks_manager:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponse("This is a custom class based view of mine!!")
