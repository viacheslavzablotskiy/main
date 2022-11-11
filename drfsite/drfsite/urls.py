
from django.contrib import admin
from django.urls import path, include, re_path
from women.views import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView
from rest_framework import routers

# router = routers.SimpleRouter
# router.register(r'women', UserBook, basename='women')
# print(router.urls)#'Доббавляется /women/'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', WomenAPIList.as_view()),
    path('api/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/local/<int:pk>/', WomenAPIDetailView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/', include('djoser.urls')),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path('api/like/', UserBook.as_view()),
    path('api/like/<int:pk>/', UserBookL.as_view()),

    # re_path(r'auth/', include('djoser.urls.authtoken')),



]
