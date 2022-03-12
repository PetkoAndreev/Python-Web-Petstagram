# from django.core.exceptions import ValidationError
import os
from os.path import join

from django.conf import settings
from django.db import models


# Custom validator - hard way
# def is_positive(value):
#     if value <= 0:
#         raise ValidationError

# age = models.IntegerField(
#     null=False,
#     blank=False,
#     validators=[
#         # is_positive, - validator with function
#         models.Min(0), - validator using models.MIN
#     ]
# )


class Pet(models.Model):
    TYPE_CHOICE_DOG = 'dog'
    TYPE_CHOICE_CAT = 'cat'
    TYPE_CHOICE_PARROT = 'parrot'

    TYPE_CHOICES = (
        (TYPE_CHOICE_DOG, 'Dog'),
        (TYPE_CHOICE_CAT, 'Cat'),
        (TYPE_CHOICE_PARROT, 'Parrot'),
    )

    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
    )
    name = models.CharField(
        max_length=6,
    )
    age = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(
        upload_to='pets',
    )

    # image_url = models.URLField()

    # # Deleting image pet when it's changed with the new one
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     db_pet = Pet.objects.get(pk=self.id)
    #     # Don't do it on this way, because it'll works only in the OS on which is developed
    #     # image_path = f'{settings.MEDIA_ROOT} / {db_pet.image.url[len("/media/"):]}'
    #     # Not a recommended variant, but it works
    #     # image_path = join(settings.MEDIA_ROOT, db_pet.image.url[len('/media/'):])
    #     image_path = join(settings.MEDIA_ROOT, str(db_pet.image))
    #     os.remove(image_path)
    #     return super().save(force_insert=force_insert, force_update=force_update, using=using,
    #                         update_fields=update_fields)


    # str method visualize data in admin panel as row, not as columns
    def __str__(self):
        return f'{self.name}, {self.age}, {self.type}'


class Like(models.Model):
    # When we have FK an object is created in main class - Model_Name_set
    # in our case - like_set is the name of the object and in that way we get the likes
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
