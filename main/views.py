
from email import message
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .forms import UserPostForm, EventForm, UpdatProfileForm, UpdatProfileImageForm , ContactUsForm
from .models import UserPost, Event, Participate
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user



@login_required(login_url='login')
def user_posts(request):
    if request.method == 'GET':
        search_post = request.GET.get('search-post', None)
        if (search_post):

            searched_posts = UserPost.objects.filter(
                wilaya=search_post)
            context = {'search_post': search_post,
                       'posts': UserPost.objects.all(),

                       'searched_posts': searched_posts}
            return render(request, 'main/user_posts_page.html', context)

    context = {'posts': UserPost.objects.all()}
    return render(request, 'main/user_posts_page.html', context)




@login_required(login_url='login')
def organisation_home(request):
    if request.method=="POST":
        c_form=ContactUsForm(request.POST)
        if c_form.is_valid():
            feedback=c_form.save(commit=False)
            feedback.save()
            return redirect('organisation-home')
    else:
        c_form=ContactUsForm()
    
    context={
        'c_form':c_form
    }
    return render(request, 'main/organisation_home_page.html',context)



def home(request):
    return render(request, 'main/index.html')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'main/sign_up.html'

    def get_success_url(self, **kwargs):
        
        return ("/login")


@unauthenticated_user
def loginpage(request):
    exists = False
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        exists = False
        if user is not None:
            login(request, user)
            if request.user.is_org == True:
                return redirect("/organisation-home")
            else:
                return redirect("/user-home")
        else:
            exists = True
            context = {'exists': exists}

            messages.error(request,'Username or password is incorrect')
    context = {'exists': exists}

    return render(request, 'main/login.html', context)



@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect("/home")



@login_required(login_url='login')
def userpost_create_view(request):
    if request.method == "POST":
        if 'postTrash' in request.POST:   
         form = UserPostForm(request.POST, request.FILES )
         if form.is_valid():
            messages.success(request,'Post created succesfully')
            post= form.save(commit=False)
            post.user= request.user
            post.save()
            return redirect('user-home') 
         else :
            messages.info(request,"Incorrect Form , Please try again")
         c_form=ContactUsForm()
        elif 'contact' in request.POST:
         c_form=ContactUsForm(request.POST)
         if c_form.is_valid():
                feedback=c_form.save(commit=False)
                feedback.save()
                return redirect('user-home')
         form=UserPostForm()
    else:
        form=UserPostForm()
        c_form=ContactUsForm()
        context= {
            'form': form,
            'c_form':c_form,
          }
    return render(request , 'main/user_home_page.html', context)




# class PostListView(ListView):
#     model = UserPost
#     template_name = 'main/user_posts_page.html'
#     context_object_name = 'posts'
#     ordering = ['-created_at']



# @login_required(login_url='login')
# def userposts_detail_view(request, url=None):

#     post = get_object_or_404(UserPost, url=url)

#     context = {'post': post,
#                }

#     return render(request, '', context)



@login_required(login_url='login')
def event_create_view(request):

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request,'Event created succesfully')
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect("/organisation-posts")
    else:
        form = EventForm()
        search_post = request.GET.get('search-post', None)
        if (search_post):

            searched_posts = UserPost.objects.filter(
                wilaya=search_post)
            context = {'search_post': search_post,
                       'posts': UserPost.objects.all(),

                       'searched_posts': searched_posts}
            return render(request, 'main/organisation_posts_page.html', context)

    context = {
        'form': form,
        'posts': UserPost.objects.all()
    }
    return render(request, 'main/organisation_posts_page.html', context)



@login_required(login_url='login')
def updat_profile(request):
    if request.method == 'POST':
        if 'changepassword' in request.POST:

            w_form = PasswordChangeForm(data=request.POST, user=request.user)

            if w_form.is_valid():
                messages.success(request,'Your password has been changed succesfully')
                w_form.save()
                update_session_auth_hash(request, w_form.user)
                return redirect('user-profile')
            else:
                messages.error(request,'something is wrong please try again')
            u_form = UpdatProfileForm(instance=request.user)
            p_form = UpdatProfileImageForm(instance=request.user.profile)
        elif 'updateprofile' in request.POST:

            u_form = UpdatProfileForm(request.POST, instance=request.user)
            p_form = UpdatProfileImageForm(request.POST,
                                           request.FILES,
                                           instance=request.user.profile)


            if u_form.is_valid() and p_form.is_valid():
                messages.success(request,'your information have been updated succesfuly')
                u_form.save()
                p_form.save()
                return redirect('user-profile')
            else:
                messages.error(request,'username already exists')
            w_form = PasswordChangeForm(user=request.user)
        elif 'delete' in request.POST:
            w_form = PasswordChangeForm(user=request.user)
            u_form = UpdatProfileForm(instance=request.user)
            p_form = UpdatProfileImageForm(instance=request.user.profile)
            if request.user.is_org == True:
                event_id = request.POST.get("event_id")
                event = Event.objects.filter(id=event_id).first()
                if event and event.user == request.user:
                    event.delete()
                    return redirect('user-profile')
            else:
                post_id = request.POST.get("post_id")
                post = UserPost.objects.filter(id=post_id).first()
                if post and post.user == request.user:
                    post.delete()
                    return redirect('user-profile')

            u_form = UpdatProfileForm(instance=request.user)
            p_form = UpdatProfileImageForm(instance=request.user.profile)
            w_form = PasswordChangeForm(user=request.user)
    else:
        u_form = UpdatProfileForm(instance=request.user)
        p_form = UpdatProfileImageForm(instance=request.user.profile)
        w_form = PasswordChangeForm(user=request.user)

    logged_in_user = request.user
    logged_in_user_posts = UserPost.objects.filter(user=logged_in_user)
    logged_in_user_events = Event.objects.filter(user=logged_in_user)
    context = {
        'w_form': w_form,
        'u_form': u_form,
        'p_form': p_form,
        'posts': logged_in_user_posts,
        'events': logged_in_user_events
    }
    if request.user.is_org == True:
        return render(request, 'main/organisation_profile.html', context)
    else:
        return render(request, 'main/user_profile.html', context)



@login_required(login_url='login')
def participate_event(request):
    user = request.user
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        event_obj = Event.objects.get(id=event_id)
        if user in event_obj.participated.all():
            event_obj.participated.remove(user)
        else:
            event_obj.participated.add(user)
        participate, created = Participate.objects.get_or_create(
            user=user, event_id=event_id)
        if not created:
            if participate.value == 'Participate':
                participate.value = 'Unparticipate'
            else:
                participate.value = 'Participate'
        participate.save()

        return redirect('user-events')
    else:
        if 'wilayabutton' in request.GET:

            search_event = request.GET.get('search-event', None)
            if (search_event):

                searched_events = Event.objects.filter(
                    wilaya=search_event)
                context = {'search_event': search_event,
                           'events': Event.objects.all(),

                           'searched_events': searched_events}
                return render(request, 'main/user_events_page.html', context)
        elif 'datebutton' in request.GET:
            search_date = request.GET.get('search-date', None)
            if (search_date):

                searched_dates = Event.objects.filter(
                    date=search_date)
                context = {'search_date': search_date,
                           'events': Event.objects.all(),

                           'searched_dates': searched_dates}
                return render(request, 'main/user_events_page.html', context)
    context = {

        'events': Event.objects.all()
    }
    return render(request, 'main/user_events_page.html', context)




@login_required(login_url='login')
def organisation_events(request):
    
    if request.method == 'GET':
        if 'wilayabutton' in request.GET:
            search_event = request.GET.get('search-event', None)
            if (search_event):

                searched_events = Event.objects.filter(
                    wilaya=search_event)
                context = {'search_event': search_event,
                           'events': Event.objects.all(),

                           'searched_events': searched_events}
                return render(request, 'main/organisation_events_page.html', context)
        elif 'datebutton' in request.GET:
            search_date = request.GET.get('search-date', None)
            if (search_date):

                searched_dates = Event.objects.filter(
                    date=search_date)
                context = {'search_date': search_date,
                           'events': Event.objects.all(),

                           'searched_dates': searched_dates}
                return render(request, 'main/organisation_events_page.html', context)

 
    context = {'events': Event.objects.all()}
    return render(request, 'main/organisation_events_page.html', context)








