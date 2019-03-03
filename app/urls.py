from django.urls import path
from . import views

from .views import CreateFamily, top_menu, FCT_view_paging

urlpatterns = [
    path('',  top_menu.as_view(), name='top_menu'),
    path('family3/',  CreateFamily.as_view(), name='family_create'),
    path('family4/',  views.family_select_create, name='family_select_create'),
    path('fct/<int:categ>/<int:order>/',  FCT_view_paging.as_view(), name='fct_view_paging'),

]
