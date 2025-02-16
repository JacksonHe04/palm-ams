from django.urls import path
from . import views

urlpatterns = [
    path('getFieldList', views.get_field_list, name='get_field_list'),
    path('addField', views.add_field, name='add_field'),
    path('updateField/<int:field_id>', views.update_field, name='update_field'),
    path('deleteField/<int:field_id>', views.delete_field, name='delete_field'),
]