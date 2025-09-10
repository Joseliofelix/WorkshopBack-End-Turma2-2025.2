from django.urls import path
from .views import EnderecoCreateView, EnderecoListView, EnderecoDetailView, EnderecoDeleteView

urlpatterns = [
    path('', EnderecoCreateView.as_view(), name='endereco_create'),
    path('list/', EnderecoListView.as_view(), name='endereco_list'),
    path('detail/<int:pk>/', EnderecoDetailView.as_view(), name='endereco_detail'),
    path('delete/<int:pk>/', EnderecoDeleteView.as_view(), name='endereco_delete'),
]
