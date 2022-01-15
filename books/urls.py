from django.urls import path
from books import views

urlpatterns = [
    path('api/books', views.book_list),
    path('api/books/1', views.book_detail),
    path('api/books/published', views.book_list_published),
]


#urlpatterns = [
#    url(r'^api/tutorials$', views.tutorial_list),
#    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
#    url(r'^api/tutorials/published$', views.tutorial_list_published)
#]
