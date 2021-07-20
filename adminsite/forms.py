from django import forms
from adminsite.models import *



class RegisterFroms(forms.ModelForm):
    class Meta:
        model = users
        fields=['User_firstname','User_lastname','user_phone','user_email','user_password']



class eventForms(forms.ModelForm):
    event_image=forms.FileField()
    class Meta:
        model = event
        fields = ["event_name", "event_image","event_date","event_time","event_location","subcat_id",]


