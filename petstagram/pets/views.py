from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.core.views import PostOnlyView
from petstagram.pets.forms import PetForm, EditPetForm
from petstagram.pets.models import Pet, Like


class ListPetsView(ListView):
    template_name = 'pets/pet_list.html'
    context_object_name = 'pets'
    model = Pet


# def list_pets(request):
#     all_pets = Pet.objects.all()
#     # Filter pets to show only cats.
#     # filter_pets = Pet.objects.filter(type=Pet.TYPE_CHOICE_CAT)
#
#     context = {
#         'pets': all_pets
#     }
#
#     return render(request, 'pets/pet_list.html', context)


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet_detail.html'
    context_object_name = 'pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = context['pet']
        pet.likes_count = pet.like_set.count()
        is_liked_by_user = pet.like_set.filter(user_id=self.request.user.id).exists()

        is_owner = pet.user == self.request.user

        context['comment_form'] = CommentForm(
            initial={
                'pet_pk': self.object.id,
            }
        )
        context['comments'] = pet.comment_set.all()
        context['is_owner'] = is_owner
        context['is_liked'] = is_liked_by_user

        return context


# def pet_details(request, pk):
#     pet = Pet.objects.get(pk=pk)
#     pet.likes_count = pet.like_set.count()
#     is_liked_by_user = pet.like_set.filter(user_id=request.user.id).exists()
#
#     # can_edit = pet.user == request.user
#     # can_delete = pet.user == request.user
#     is_owner = pet.user == request.user
#
#     context = {
#         'pet': pet,
#         'comment_form': CommentForm(
#             initial={
#                 'pet_pk': pk,
#             }
#         ),
#         # Get all comments
#         'comments': pet.comment_set.all(),
#         'is_owner': is_owner,
#         'is_liked': is_liked_by_user,
#     }
#
#     return render(request, 'pets/pet_detail.html', context)


# This is used if we develop the comment login in views, not in the form.
# def comment_pet(request, pk):
#     pet = Pet.objects.get(pk=pk)
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         comment = Comment(
#             comment=form.cleaned_data['comment'],
#             pet=pet,
#         )
#         comment.save()
#
#     return redirect('pet details', pet.id)

# Better to be done with Function view - looks simplyier
class CommentPetView(LoginRequiredMixin, PostOnlyView):
    form_class = CommentForm

    def form_valid(self, form):
        pet = Pet.objects.get(pk=self.kwargs['pk'])
        comment = Comment(
            comment=form.cleaned_data['comment'],
            pet=pet,
            user=self.request.user,
        )
        comment.save()
        return redirect('pet details', pet.id)


# @login_required
# def comment_pet(request, pk):
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         comment = form.save(commit=False)
#         comment.user = request.user
#         comment.save()
#
#     return redirect('pet details', pk)

class LikePetView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pet = Pet.objects.get(pk=self.kwargs['pk'])
        like_object_by_user = pet.like_set.filter(user_id=self.request.user.id).first()
        if like_object_by_user:
            like_object_by_user.delete()
        else:
            like = Like(
                pet=pet,
                user=self.request.user,
            )
            like.save()
        return redirect('pet details', pet.id)


# @login_required
# def like_pet(request, pk):
#     pet = Pet.objects.get(pk=pk)
#     # Added logic to check if the user liked the pet
#     like_object_by_user = pet.like_set.filter(user_id=request.user.id).first()
#     if like_object_by_user:
#         like_object_by_user.delete()
#     else:
#         like = Like(
#             pet=pet,
#             user=request.user,
#         )
#         like.save()
#     return redirect('pet details', pet.id)


class CreatePetView(LoginRequiredMixin, CreateView):
    model = Pet
    template_name = 'pets/pet_create.html'
    form_class = PetForm
    # fields = ('name', 'description', 'image', 'age', 'type',)
    success_url = reverse_lazy('list pets')

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()

        return super().form_valid(form)


# @login_required
# def create_pet(request):
#     if request.method == 'POST':
#         form = PetForm(request.POST, request.FILES)
#         if form.is_valid():
#             pet = form.save(commit=False)
#             pet.user = request.user
#             pet.save()
#             return redirect('list pets')
#     else:
#         form = PetForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'pets/pet_create.html', context)

class EditPetView(UpdateView):
    model = Pet
    template_name = 'pets/pet_edit.html'
    form_class = EditPetForm
    success_url = reverse_lazy('list pets')


# @login_required
# def edit_pet(request, pk):
#     pet = Pet.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = EditPetForm(request.POST, request.FILES, instance=pet)
#         if form.is_valid():
#             form.save()
#             return redirect('list pets')
#     else:
#         form = EditPetForm(instance=pet)
#
#     context = {
#         'form': form,
#         'pet': pet,
#     }
#
#     return render(request, 'pets/pet_edit.html', context)

class DeletePetView(LoginRequiredMixin, DeleteView):
    template_name = 'pets/pet_delete.html'
    model = Pet
    success_url = reverse_lazy('list pets')

# @login_required
# def delete_pet(request, pk):
#     pet = Pet.objects.get(pk=pk)
#     if request.method == 'POST':
#         pet.delete()
#         return redirect('list pets')
#     else:
#         context = {
#             'pet': pet,
#         }
#         return render(request, 'pets/pet_delete.html', context)
