from django.views.generic import UpdateView
from .models import Task
from django.urls import reverse_lazy


class UpdateViewCustom(UpdateView):
    """Here we are building our own Update View to be used generically"""
    url_name = ""

    template_name = 'tasks_manager/update_view_custom.html'

    fields = '__all__'

    # alternatively:
    def get_success_url(self):
        #print(self.__dict__)
        return reverse_lazy(self.success_url, args=[self.kwargs['pk']])

    def get_context_data(self, **kwargs):
        """how to override what the class based view is doing to our data"""
        context = super(UpdateViewCustom, self).get_context_data(**kwargs)

        # get the verbose name of the defined model

        #print(self.model._meta.verbose_name)

        context['model_name'] = self.model._meta.verbose_name
        context['url_name'] = self.url_name
        # we are sending the url name and the model name to the template

        return context
