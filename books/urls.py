from django.urls import path
from .views import BookListApiView, BookDetailApiView, BookDeleteApiview, BookUpdateApiview, \
    BookCreateApiView, BookListCreateApiView, BookListCreateNewApiView

urlpatterns = [
    path('books/', BookListApiView.as_view(),),
    path('booklistcreate/', BookListCreateNewApiView.as_view(),),
    path('bookupdatedelete/<int:pk>/', BookListCreateApiView.as_view(),),
    path('books/create/', BookCreateApiView.as_view(),),
    path('books/<int:pk>/', BookDetailApiView.as_view(),),
    path('books/<int:pk>/update', BookUpdateApiview.as_view(),),
    path('books/<int:pk>/delete', BookDeleteApiview.as_view(),),

]