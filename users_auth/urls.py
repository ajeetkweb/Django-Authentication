from django.urls import path, include
from users_auth import views
urlpatterns = [
    path('create_user/', views.create_user),
    path('', views.list_users),
    path('user_detail/<int:pk>', views.user_details),

    # class-based end-points

    path('listUsers/', views.ListUsers.as_view()),
    path('user_info/<int:pk>', views.UserInfo.as_view()),

    # generics views end-points

    path('list_create_users/', views.ListCreateUserViews.as_view()),
    path('retrieve_update_user/<int:pk>', views.RetrieveUpdateUserAPIView.as_view()),



]
