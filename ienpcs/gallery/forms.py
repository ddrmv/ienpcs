from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    invitation_code = forms.CharField(
        label="Invitation code:",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "ex: 537b048d7f14e109c1b...",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "..."
        self.fields["username"].label = "Username"
        self.fields[
            "username"
        ].help_text = '<span class="form-text text-muted">Up to 150 characters. Letters, digits and @.+-_ only.</span>'

        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["placeholder"] = "..."
        self.fields["email"].label = "Email"
        self.fields[
            "email"
        ].help_text = '<span class="form-text text-muted">Enter a vaild email.</span>'

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "..."
        self.fields["password1"].label = "Password"
        self.fields[
            "password1"
        ].help_text = "<ul class=\"form-text text-muted small\"><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>"

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "..."
        self.fields["password2"].label = "Confirm Password"
        self.fields[
            "password2"
        ].help_text = '<span class="form-text text-muted">Enter the same password as before, for verification.</span>'
