from django.urls import path, re_path as url
from doc_app import views 

urlpatterns = [
    url(r'^contacts/add$',views.Contacts.as_view(),name='add-contact'),
]