from django import forms

from petstagram.core.forms import BootstrapFormMixin
from petstagram.pets.models import Pet


class PetForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        # Add additional class for name field of the form to show
        # that we can add additional class not only from Bootstrap Mixin
        # widgets = {
        #     'name': forms.TextInput(
        #         attrs={
        #             'class': 'my-class'
        #         }
        #     )
        # }


class EditPetForm(PetForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'disabled': 'disabled'
                }
            )
        }
