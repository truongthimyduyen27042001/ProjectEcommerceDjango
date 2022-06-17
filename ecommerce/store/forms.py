from django import forms

class registerForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'form_username'}))
    # email = forms.EmailField()
    email= forms.CharField(widget= forms.EmailInput
                           (attrs={'class':'form-control',
				   'id':'form_email'}))

    password = forms.CharField(max_length=20,widget=forms.PasswordInput
                               (attrs={'class': 'form-control',
                                       'id':'form_password'}))
    
class loginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'form_username'}))
    password = forms.CharField(max_length=20,widget=forms.PasswordInput
                               (attrs={'class': 'form-control',
                                       'id':'form_password'}))