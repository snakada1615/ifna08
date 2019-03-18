from django.urls import path
from . import views

from .views import FCT_view_paging, FamilyCreateView
from .views import FamilyDeleteView, FamilyCreateView, FamilyUpdateView
from .views import DietCreateView, DietUpdateView, DietListView, DietDeleteView
from .views import FamilyList_ListView, FamilyList_CreateView, FamilyList_DeleteView, FamilyList_UpdateView, SelectMenu, family_list

urlpatterns = [
    path('family/list/<int:familyid>',  family_list.as_view(), name='family_list'),
    path('family/create/<int:familyid>/', FamilyCreateView.as_view(), name='family_create'),
    path('family/update/<int:familyid>/<int:pk>/', FamilyUpdateView.as_view(), name='family_update'),
    path('family/delete/<int:familyid>/<int:pk>/', FamilyDeleteView.as_view(), name='family_delete'),
    path('fct/<int:categ>/<int:order>/',  FCT_view_paging.as_view(), name='fct_view_paging'),
    path('diet/list/<int:familyid>/',  DietListView.as_view(), name='diet_index'),
    path('diet/create/<int:familyid>/', DietCreateView.as_view(), name='diet_create'),
    path('diet/delete/<int:familyid>/<int:pk>/', DietDeleteView.as_view(), name='diet_delete'),
    path('diet/update/<int:familyid>/<int:pk>/', DietUpdateView.as_view(), name='diet_update'),
    path('FamilyList/list/',  FamilyList_ListView.as_view(), name='FamilyList_index'),
    path('FamilyList/create/', FamilyList_CreateView.as_view(), name='FamilyList_create'),
    path('FamilyList/update/<int:pk>/', FamilyList_UpdateView.as_view(), name='FamilyList_update'),
    path('FamilyList/delete/<int:pk>/', FamilyList_DeleteView.as_view(), name='FamilyList_delete'),
    path('selectfamily/', SelectMenu.as_view(), name='select_family'),
]
