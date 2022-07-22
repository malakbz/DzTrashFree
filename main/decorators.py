from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_org == True:
                return redirect("organisation-home")
            else:
                return redirect("user-home")

        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


# def admin_only(view_func):
#     def wrapper_func(request, *args , **kwargs):
#          group = None
#          if request.user.groups.exists():
#              group =request.user.groups.all()[0].name
#          if group == 'normalUsers' : 
#           return redirect ('user_home')
#          if group =='admin':
#              return view_func(request, *args, **kwargs)
         
#     return wrapper_func