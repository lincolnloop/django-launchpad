from django import forms
from . import models

class EmailInput(forms.widgets.TextInput):
    input_type = 'email'

class MemberForm(forms.ModelForm):
    email = forms.CharField(widget=EmailInput(
                            {"placeholder": "you@example.com" }))

    class Meta:
        model = models.Member
        exclude = ('is_subscribed', 'unsubscribed_time')
