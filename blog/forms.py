from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Contact
# from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

	class Meta(UserCreationForm):
		model = User
		# fields = ('username', 'bio', 'location', 'birth_date','password1', 'password2',)
		fields = ('username', 'firstname', 'lastname', 'bio', 'location', 'birth_date', 'email')

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = "__all__"


