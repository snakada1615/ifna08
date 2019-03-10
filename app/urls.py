from django.urls import path
from . import views

from .views import CreateFamily, top_menu, FCT_view_paging, FamilyFilterView, FamilyDetailView, FamilyCreateView
from .views import FamilyUpdateView, FamilyDeleteView, family_viewonly, FamilyEditView, FamiliesAddView
from .views import DietCreateView, DietUpdateView, DietListView, DietDeleteView, DietDetailView

urlpatterns = [
    path('',  top_menu.as_view(), name='top_menu'),
    path('family3/',  CreateFamily.as_view(), name='family_create'),
    path('family/<int:familyid>',  family_viewonly.as_view(), name='family_viewonly'),
    path('family/edit/<int:familyid>',  FamilyEditView.as_view(), name='family_edit'),
    path('family/add',  FamiliesAddView.as_view(), name='families_add'),
    path('family/',  views.family_select_create, name='family_select_create'),
    path('fct/<int:categ>/<int:order>/',  FCT_view_paging.as_view(), name='fct_view_paging'),
    path('list/',  FamilyFilterView.as_view(), name='index'),
    path('detail/<int:pk>/', FamilyDetailView.as_view(), name='detail'),
    path('create/', FamilyCreateView.as_view(), name='create'),
    path('update/<int:pk>/', FamilyUpdateView.as_view(), name='update'),
    path('delete/<int:familyid>/<int:pk>/', FamilyDeleteView.as_view(), name='delete'),
    path('diet/list/<int:familyid>/',  DietListView.as_view(), name='diet_index'),
    path('diet/create/<int:familyid>/', DietCreateView.as_view(), name='diet_create'),
    path('diet/detail/<int:familyid>/<int:pk>/', DietDetailView.as_view(), name='diet_detail'),
    path('diet/update/<int:familyid>/<int:pk>/', DietUpdateView.as_view(), name='diet_update'),
    path('diet/delete/<int:familyid>/<int:pk>/', DietDeleteView.as_view(), name='diet_delete'),
]
