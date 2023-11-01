from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

# Create your views here.

# def task(request):
#     return HttpResponse('to do list')

class CustomeLoginView(LoginView):
    template_name = 'base/login.html'
    fields='__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        # context['name'] = 'kaushal' # this will pass data to html page
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context

class TaskDetails(LoginRequiredMixin,DetailView):
    model=Task
    context_object_name = 'task'
    template_name='base/task.html'

class TaskCreate(LoginRequiredMixin,CreateView):
    # used model forms 
    model = Task
    # fields = '__all__' # this will show all the value that created in model class
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self,form): # auto seleted login user and create task for him
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    # fields = '__all__'
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    