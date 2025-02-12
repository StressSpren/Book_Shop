from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()                    # router class in DRF that auto generates url patterns
router.register(r'books', views.BookViewSet)        # r'books' returns a raw string called books to avoid escape characters
router.register(r'author', views.AuthorViewSet)     # Registers the AuthorViewSet under the 'author/' endpoint
router.register(r'category', views.CategoryViewSet)




urlpatterns = [
    path('', include(router.urls)),
]