from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Pc


class AuthenticateUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")


class CreatePcForm(forms.ModelForm):
    class Meta:
        model = Pc
        fields = (
            "name",
            "adnd_class",
            "race",
            "alignment",
            "str",
            "str_percentile",
            "dex",
            "con",
            "int",
            "wis",
            "cha",
        )

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)

        help_text_dict = {
            "name": "Name is required.",
            "adnd_class": "Ex: Fighter, Mage, Kensai/Illusionist/Swashbuckler",
            "race": "Ex: Human, Dwarf, Drow, Hamster",
            "alignment": "Ex: Neutral Good, Evil",
            "str": "Usually 3 to 18",
            "str_percentile": "For fighter classes, 1 to 100",
            "dex": "Usually 3 to 18",
            "con": "Usually 3 to 18",
            "int": "Usually 3 to 18",
            "wis": "Usually 3 to 18",
            "cha": "Usually 3 to 18",
        }

        for field in self.fields.keys():
            self.fields[
                field
            ].help_text = f'<span class="form-text">{ help_text_dict[field] }</span>'

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

        self.fields["name"].label = "Name"
        self.fields["adnd_class"].label = "Class"
        self.fields["race"].label = "Race"
        self.fields["alignment"].label = "Alignment"
        self.fields["str"].label = "Strength"
        self.fields["str_percentile"].label = "Str /100"
        self.fields["dex"].label = "Dexterity"
        self.fields["con"].label = "Constitution"
        self.fields["int"].label = "Intelligence"
        self.fields["wis"].label = "Wisdom"
        self.fields["cha"].label = "Charisma"


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
