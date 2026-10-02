from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import InsuranceApplication, ContactMessage


class InsuranceApplicationForm(forms.ModelForm):

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user and user.is_authenticated:
            self.fields['email'].initial = user.email
            self.fields['email'].disabled = True

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if not phone.isdigit():
            raise forms.ValidationError(
                'Phone number must contain only digits.'
            )

        if len(phone) != 10:
            raise forms.ValidationError(
                'Phone number must be exactly 10 digits.'
            )

        return phone

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']

        from datetime import date

        if date_of_birth > date.today():
            raise forms.ValidationError(
                'Date of birth cannot be in the future.'
            )

        return date_of_birth

    class Meta:
        model = InsuranceApplication
        fields = [
            'full_name',
            'email',
            'phone',
            'date_of_birth',
            'address',
        ]

        widgets = {
            'full_name': forms.TextInput(
                attrs={'placeholder': 'Enter your full name'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Enter your email'}
            ),
            'phone': forms.TextInput(
                attrs={'placeholder': 'Enter your phone number'}
            ),
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'address': forms.Textarea(
                attrs={
                    'placeholder': 'Enter your address',
                    'rows': 4
                }
            ),
        }


class ContactMessageForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = [
            'name',
            'email',
            'phone',
            'message',
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter your name'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Enter your email'}
            ),
            'phone': forms.TextInput(
                attrs={'placeholder': 'Enter your phone number'}
            ),
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Write your message...',
                    'rows': 5
                }
            ),
        }


class SignupForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter password'}
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Enter username'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Enter email'}
            ),
        }

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'This username is already taken.'
            )

        return username

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'An account with this email already exists.'
            )

        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        validate_password(password)
        return password
