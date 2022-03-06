from django.urls import path
from .views.character_views import CharactersView, CharacterDetailView
from .views.user_views import SignUpView, SignInView, SignOutView, ChangePasswordView

urlpatterns = [
  	# Restful routing
    path('characters/', CharactersView.as_view(), name='characters'),
    path('characters/create/', CharactersView.as_view(), name='characters-create'),
    path('characters/<int:pk>/', CharacterDetailView.as_view(), name='character_detail'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('change-pw/', ChangePasswordView.as_view(), name='change-pw')
]
