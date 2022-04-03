from django.urls import path

from petstagram.pets.views import PetDetailsView, CommentPetView, ListPetsView, CreatePetView, EditPetView, \
    DeletePetView, LikePetView

urlpatterns = [
    # path('', list_pets, name='list pets'),
    path('', ListPetsView.as_view(), name='list pets'),
    # path('details/<int:pk>', pet_details, name='pet details'),
    path('details/<int:pk>', PetDetailsView.as_view(), name='pet details'),
    # path('like/<int:pk>', like_pet, name='like pet'),
    path('like/<int:pk>', LikePetView.as_view(), name='like pet'),
    # path('create/', create_pet, name='create pet'),
    path('create/', CreatePetView.as_view(), name='create pet'),
    # path('edit/<int:pk>', edit_pet, name='edit pet'),
    path('edit/<int:pk>', EditPetView.as_view(), name='edit pet'),
    # path('delete/<int:pk>', delete_pet, name='delete pet'),
    path('delete/<int:pk>', DeletePetView.as_view(), name='delete pet'),
    # path('comment/<int:pk>', comment_pet, name='comment pet'),
    path('comment/<int:pk>', CommentPetView.as_view(), name='comment pet'),
]
