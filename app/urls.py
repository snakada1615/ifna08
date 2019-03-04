from django.urls import path
from . import views

from .views import CreateFamily, top_menu, FCT_view_paging, FamilyFilterView, FamilyDetailView, FamilyCreateView
from .views import FamilyUpdateView, FamilyDeleteView

urlpatterns = [
    path('',  top_menu.as_view(), name='top_menu'),
    path('family3/',  CreateFamily.as_view(), name='family_create'),
    path('family4/',  views.family_select_create, name='family_select_create'),
    path('fct/<int:categ>/<int:order>/',  FCT_view_paging.as_view(), name='fct_view_paging'),
    path('list/',  FamilyFilterView.as_view(), name='index'),
    path('detail/<int:pk>/', FamilyDetailView.as_view(), name='detail'),
    path('create/', FamilyCreateView.as_view(), name='create'),
    path('update/<int:pk>/', FamilyUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', FamilyDeleteView.as_view(), name='delete'),

]