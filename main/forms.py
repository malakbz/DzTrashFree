from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ContactUs, User
from .models import UserPost, Event, Profile
from django.contrib.admin.widgets import AdminDateWidget
#from .widgets import BootstrapDateTimePickerInput
from django.forms.widgets import DateInput


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'wilaya', 'email', 'is_org', 'org_document')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ('username', 'wilaya', 'email', 'is_org', 'org_document')


class UserPostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ('title', 'description', 'wilaya', 'image', 'location')


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'date',
                  'wilaya', 'image', 'location')
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }


class UpdatProfileForm(CustomUserChangeForm):
    # edit_profile = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = User
        fields = ['username', 'wilaya', 'email']


class UpdatProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields=['message_name','message_email','message']







