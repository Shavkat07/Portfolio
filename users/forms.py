from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from django import forms
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'aria-label': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'aria-label': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'aria-label': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'aria-label': 'Email Address'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'aria-label': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'aria-label': 'Confirm Password'}))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    # def save(self, commit=True):
    #     user = super(UserRegistrationForm, self).save(commit=True)
    #     expiration = now() + timedelta(hours=48)
    #     record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
    #     record.send_verification_email()
    #     return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
