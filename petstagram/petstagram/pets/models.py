# from django.core.exceptions import ValidationError
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
    image_url = models.URLField()

    # str method visualize data in admin panel as row, not as columns
    # def __str__(self):
    #     return f'{self.name}, {self.age}, {self.type}'


class Like(models.Model):
    # When we have FK an object is created in main class - Model_Name_set
    # in our case - like_set is the name of the object and in that way we get the likes
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
