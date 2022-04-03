import os
from os.path import join

from django import forms
from django.conf import settings

from petstagram.core.forms import BootstrapFormMixin
from petstagram.pets.models import Pet


class PetForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ('user',)
        # fields = '__all__'
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
    # Deleting image pet when it's changed with the new one
    def save(self, commit=True):
        db_pet = Pet.objects.get(pk=self.instance.id)
        if commit:
            # Don't do it on this way, because it'll works only in the OS on which is developed
            # image_path = f'{settings.MEDIA_ROOT} / {db_pet.image.url[len("/media/"):]}'
            # Not a reccomended variant, but it works
            # image_path = join(settings.MEDIA_ROOT, db_pet.image.url[len('/media/'):])
            image_path = join(settings.MEDIA_ROOT, str(db_pet.image))
            os.remove(image_path)
        return super().save(commit)

    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }
