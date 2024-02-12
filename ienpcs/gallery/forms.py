from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Pc
from .validators import web_image_size


class AuthenticateUserForm(AuthenticationForm):
    """Form used for logging in."""

    class Meta:
        model = User
        fields = ("username", "password")


class ContactForm(forms.Form):
    """Form used to send an email to the site admin."""

    name = forms.CharField(max_length=80)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class CreatePcForm(forms.ModelForm):
    """Form used for creating and updating Player Characters for party."""

    class Meta:
        model = Pc
        fields = (
            "name",
            "web_image",
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
            "web_image": "Image should be 110x170px.",
            "adnd_class": "Ex: Fighter, Mage, F/M, Kensai/Illusionist/Swashbuckler",
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

        label_dict = {
            "name": "Name",
            "web_image": "Portrait",
            "adnd_class": "Class",
            "race": "Race",
            "alignment": "Alignment",
            "str": "Strength",
            "str_percentile": "Str /100",
            "dex": "Dexterity",
            "con": "Constitution",
            "int": "Intelligence",
            "wis": "Wisdom",
            "cha": "Charisma",
        }

        # Add form-text to all fields from help_text_dict, add form-control, labels
        for field_key, field_value in self.fields.items():
            field_value.widget.attrs["class"] = "form-control"
            field_value.label = label_dict[field_key]
            help_str = f'<span class="form-text">{ help_text_dict[field_key] }</span>'
            field_value.help_text = help_str

        # Add custom validators
        self.fields["web_image"].validators.append(web_image_size)


class SignUpForm(UserCreationForm):
    """Form used for signing up new users."""

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

        help_text_dict = {
            "username": "Up to 150 characters. Letters, digits and @.+-_ only.",
            "email": "Enter a vaild email.",
            "password1": "PLACEHOLDER",  # Will be overridden
            "password2": "Enter the same password as before, for verification.",
        }

        label_dict = {
            "username": "Username",
            "email": "Email",
            "password1": "Password",
            "password2": "Confirm Password",
        }

        for field in ["username", "email", "password1", "password2"]:
            field_value = self.fields[field]
            field_value.widget.attrs["class"] = "form-control"
            field_value.widget.attrs["placeholder"] = "..."
            field_value.label = label_dict[field]
            help_str = (
                f'<span class="form-text text-muted">{ help_text_dict[field] }</span>'
            )
            field_value.help_text = help_str

        # Override parrword1 help text, differently styled by bootstrap
        self.fields["password1"].help_text = (
            '<ul class="form-text text-muted small">'
            "<li>Your password can't be too similar to your other personal information.</li>"
            "<li>Your password must contain at least 8 characters.</li>"
            "<li>Your password can't be a commonly used password.</li>"
            "<li>Your password can't be entirely numeric.</li>"
            "</ul>"
        )
