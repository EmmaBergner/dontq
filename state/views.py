from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import State
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

@method_decorator(login_required, name='get')
class ControlPage(View):
    model = State
    template_name = 'business.html'
    template_name = 'user.html'

    def get(self, request, *args, **kwargs):
        queryset = State.objects.all()
        state = get_object_or_404(queryset, id=2)
        if (request.GET.get('mybtn') and state.current > 0):
            state.current = state.current-1
        if (request.GET.get('mybtng')):
            state.current = state.current+1
        if (request.GET.get('myreset')):
            state.current = 0
            state.next = 0
        state.save()
        context = {
            'current': state.current
        }
        return render(request, 'business.html', context)


class UserPage(View):
    model = State
    template_name = 'business.html'
    template_name = 'user.html'

    def get(self, request, *args, **kwargs):
        queryset = State.objects.all()
        state = get_object_or_404(queryset, id=2)
        state.next = state.next+1
        state.save()
        return redirect('/usertwo?' + str(state.next))


class UserTwoPage(View):
    model = State
    # template_name = 'user.html'

    def get(self, request, *args, **kwargs):
        queryset = State.objects.all()
        state = get_object_or_404(queryset, id=2)
        ticket =  request.get_full_path().split("?")[1]
        context = {
            'current': state.current,
            'ticket': ticket,
            'remaining' : int(ticket) - state.current,
        }
        return render(request, 'user.html', context)


class Login(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')