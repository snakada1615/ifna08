from django.views.generic import TemplateView, CreateView
from django.views.generic import ListView
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages  # メッセージフレームワーク
from django.db.models import Sum
from django_filters.views import FilterView

from .filters import FamilyFilter
from .models import FCT, Family, DRI, FamilyList
from .forms import Order_Key_Form, Families, Family_Create_Form, FamilyForm


class family_viewonly(LoginRequiredMixin, ListView):
    template_name = 'app/family_viewonly.html'  # この行でテンプレート指定
    context_object_name = 'families'
    model = Family

    def get_queryset(self):
        queryset = super().get_queryset().filter(familyid = self.kwargs['familyid'])
        return queryset

class FCT_view_paging(LoginRequiredMixin, ListView):
    template_name = 'app/FCT_Show_paging.html'  # この行でテンプレート指定
    context_object_name = 'foods1'
    model = FCT
    paginate_by = 15
    CHOICE =	{
      0: 'Food_name',
      1: '-Protein',
      2: '-FE',
      3: '-VITA_RAE',
    }
    CATEG = {
		1: 'Cereals and their products',
		2: 'Roots, tubers and their products',
		3: 'Legumes and their products',
		4: 'Vegetables and their products',
		5: 'Fruits and their products',
		6: 'Nuts, Seeds and their products',
		7: 'Meat, poultry and their products',
		8: 'Eggs and their products',
		9: 'Fish and their products',
		10: 'Milk and their products',
		11: 'Bevarages and their products',
		12: 'Miscellaneous',
    }

    def get_queryset(self):
        queryset = super().get_queryset().filter(food_grp_id = self.kwargs['categ']).order_by(self.CHOICE[self.kwargs['order']])
        return queryset

    def get_context_data(self, **kwargs):
        form = Order_Key_Form()
        context = super().get_context_data(**kwargs)
        context['order1'] = form
        context['categ_id'] = self.kwargs['categ']
        context['categ'] = self.CATEG[self.kwargs['categ']]
        return context

    def post(self, request, *args, **kwargs):
        if 'btn2' in request.POST:
            return redirect('top_menu')


# Create your views here.
# 検索一覧画面

# 検索一覧画面
class FamilyFilterView(LoginRequiredMixin, FilterView):
    model = Family

    # デフォルトの並び順を新しい順とする
    queryset = Family.objects.all().order_by('-created_at')

    # django-filter用設定
    filterset_class = FamilyFilter
    strict = False

    # 1ページあたりの表示件数
    paginate_by = 10

    # 検索条件をセッションに保存する
    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)

# 詳細画面
class FamilyDetailView(LoginRequiredMixin, DetailView):
    model = Family


# 登録画面
class FamilyCreateView(LoginRequiredMixin, CreateView):
    model = Family
    form_class = Family_Create_Form
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        form = Family_Create_Form(request.POST)
        if form.is_valid():
            family=form.save()
            family.save()

            family_p = Family.objects.aggregate(Sum('protein'))
            family_v = Family.objects.aggregate(Sum('vita'))
            family_f = Family.objects.aggregate(Sum('fe'))
            mydata = self.request.session.get('myword')
            myid = FamilyList.objects.get(name = mydata).id
            rec = FamilyList.objects.filter(id = myid).first()
            rec.protein = family_p['protein__sum']
            rec.vita = family_v['vita__sum']
            rec.fe = family_f['fe__sum']
            rec.save()
        return redirect('index')


# 更新画面
class FamilyUpdateView(LoginRequiredMixin, UpdateView):
    model = Family
    form_class = FamilyForm
    success_url = reverse_lazy('index')


# 削除画面
class FamilyDeleteView(LoginRequiredMixin, DeleteView):
    model = Family
    success_url = reverse_lazy('family_create')


class top_menu(LoginRequiredMixin, TemplateView):
    template_name = "app/topmenu.html"  # この行でテンプレート指定


class CreateFamily(LoginRequiredMixin, CreateView):
    template_name = 'app/family_create.html'
    form_class = Family_Create_Form
    success_url = 'family_create'

    def get_context_data(self, **kwargs):
        mydata = self.request.session.get('myword')
        myid = FamilyList.objects.get(name = mydata).id
        dri_p = FamilyList.objects.get(name = mydata).protein
        dri_v = FamilyList.objects.get(name = mydata).vita
        dri_f = FamilyList.objects.get(name = mydata).fe
        context = super().get_context_data(**kwargs)
        form = Family_Create_Form(initial={'name': mydata, 'familyid' : myid})
        context['form'] = form
        context['name'] = mydata
        context['dri_p'] = dri_p
        context['dri_v'] = dri_v
        context['dri_f'] = dri_f
        context["families"] = Family.objects.filter(name = mydata)
        return context

    def post(self, request, *args, **kwargs):
        if 'btn1' in request.POST:
            form = Family_Create_Form(request.POST)
            if form.is_valid():
                family=form.save()
                family.save()

                family_p = Family.objects.aggregate(Sum('protein'))
                family_v = Family.objects.aggregate(Sum('vita'))
                family_f = Family.objects.aggregate(Sum('fe'))
                mydata = self.request.session.get('myword')
                myid = FamilyList.objects.get(name = mydata).id
                rec = FamilyList.objects.filter(id = myid).first()
                rec.protein = family_p['protein__sum']
                rec.vita = family_v['vita__sum']
                rec.fe = family_f['fe__sum']
                rec.save()
            return redirect('family_create')

        if 'btn2' in request.POST:
            return redirect('family_select_create')

        if 'btn3' in request.POST:
            return redirect('top_menu')



def family_select_create(request):

    if request.method == "POST":
        families = Families(data=request.POST)
        if families.is_valid():
#            address = "family/" + request.POST.get('familyname')
            request.session['myword'] = request.POST.get('familyname')
            return HttpResponseRedirect('/family3/')
    else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
        families = Families()

    return render(request, 'app/family_select.html', {
        'families' : families,
    })
