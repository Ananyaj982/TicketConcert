from django.http import HttpResponse
from django.shortcuts import redirect

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        #if group == 'customer':
            #return redirect('user-page')

        if group == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('question_new')

    return wrapper_function

def admin_only1(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        #if group == 'customer':
            #return redirect('user-page')

        if group == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('doubt')

    return wrapper_function

