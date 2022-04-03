from django.urls import path

from petstagram.accounts.views import logout_user, RegisterView, ProfileDetailsView, LoginUserView

urlpatterns = (
    # path('login/', login_user, name='log in user'),
    path('login/', LoginUserView.as_view(), name='log in user'),
    path('logout/', logout_user, name='log out user'),
    # path('register/', register_user, name='register user'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('profile/', ProfileDetailsView.as_view(), name='profile details'),
)
