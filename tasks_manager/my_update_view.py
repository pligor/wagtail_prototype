from django.views.generic import UpdateView
from .models import Task
from django.urls import reverse_lazy


class MyUpdateView(UpdateView):
    model = Task

    template_name = 'tasks_manager/update_task.html'

    fields = '__all__'

    # success_url = reverse_lazy('home'),
    # alternatively:
    def get_success_url(self):
        # print(self.__dict__)
        return reverse_lazy('update_task', args=[self.kwargs['pk']])


