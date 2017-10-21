from django import forms
from django.contrib.auth.models import User
from .models import Profile, Material

# Generate registration form
class UserRegistrationForm(forms.ModelForm): 
	password = forms.CharField(label='Password.', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat password.', widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username','first_name','email')	
	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Password does not match the confirm password.')
		return cd['password2']
	
# Generate login form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
	
# Generate user_edit form
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')
		
# Generate profile_edit form
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth','photo')
		
# Generate edit form
class MaterialEdit(forms.ModelForm):
	class Meta:
		model = Material
		fields = ('name','description','notes','supplier','price','currency')