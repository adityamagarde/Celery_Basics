from django import forms
from .tasks import send_email_task

class ReviewForm(forms.Form):
    name = forms.CharField(
        label='Firstname', min_length=4, max_length=59, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-firstname'}))
    email = forms.EmailField(
        label='Email', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'E-Mail', 'id': 'form-email'}))
    review = forms.CharField(
        label='Review', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

    def send_email(self):
        send_email_task.delay(
            self.cleaned_data['name'], self.cleaned_data['email'], self.cleaned_data['review'])
