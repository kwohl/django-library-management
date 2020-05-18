from django.urls import path, include
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('book/form', book_form, name='book_form'),
    path('librarians/', librarian_list, name='librarians'),
    path('libraries/', library_list, name='libraries'),
    path('library/form', library_form, name='library_form'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
]