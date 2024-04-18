
from django import forms
from .models import court

class CourtForm(forms.ModelForm):

    startTime = forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget(date_attrs={'type':'data'},time_attrs={'type':'time'}))
    endTime = forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget(date_attrs={'type':'data'},time_attrs={'type':'time'}))

    class Meta:
        model = court
        fields = ['courtName','startTime','endTime','amount','available']