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
from .forms import Order_Key_Form, Families, Family_Create_Form, FamilyForm, FamiliesAddForm

class FamilyEditView(LoginRequiredMixin, CreateView):
    template_name = 'app/family_edit.html'
    form_class = Family_Create_Form

    def get_context_data(self, **kwargs):
        myid = self.kwargs['familyid']
        mydata = FamilyList.objects.get(id = myid)
        context = super().get_context_data(**kwargs)
        form = Family_Create_Form(initial={'name': mydata, 'familyid' : myid})
        context['form'] = form
        context['name'] = mydata
        context['myid'] = myid
        context["families"] = Family.objects.filter(familyid = self.kwargs['familyid']).order_by('age')
        return context

    def get_success_url(self, **kwargs):
        if  kwargs != None:
            return reverse_lazy('family_edit', kwargs = {'familyid': self.kwargs['familyid']})
        else:
            return reverse_lazy('family_edit', args = (self.object.id,))

    def post(self, request, *args, **kwargs):
        if 'btn1' in request.POST:
            form = Family_Create_Form(request.POST)
            if form.is_valid():
                family=form.save()
                family.save()

                myid = self.kwargs['familyid']
                family_p = Family.objects.filter(familyid = myid).aggregate(Sum('protein'))
                family_v = Family.objects.filter(familyid = myid).aggregate(Sum('vita'))
                family_f = Family.objects.filter(familyid = myid).aggregate(Sum('fe'))
                mydata = FamilyList.objects.get(id = myid).name
                rec = FamilyList.objects.filter(id = myid).first()
                rec.protein = family_p['protein__sum']
                rec.vita = family_v['vita__sum']
                rec.fe = family_f['fe__sum']
                rec.save()
            return redirect('family_edit', familyid = myid)
#            return redirect('family')


class family_viewonly(LoginRequiredMixin, ListView):
    template_name = 'app/family_viewonly.html'  # この行でテンプレート指定
    context_object_name = 'families'
    model = Family

    def get_queryset(self):
        queryset = super().get_queryset().filter(familyid = self.kwargs['familyid']).order_by('age')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = FamilyList.objects.get(id = self.kwargs['familyid'])
        context['myid'] = FamilyList.objects.get(id = self.kwargs['familyid']).id
        context['dri_p'] = FamilyList.objects.get(id = self.kwargs['familyid']).protein
        context['dri_v'] = FamilyList.objects.get(id = self.kwargs['familyid']).vita
        context['dri_f'] = FamilyList.objects.get(id = self.kwargs['familyid']).fe
        return context

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['familyid'] = self.kwargs['familyid']
        return context

    def get_success_url(self, **kwargs):
        if  kwargs != None:
            return reverse_lazy('family_edit', kwargs = {'familyid': self.kwargs['familyid']})
        else:
            return reverse_lazy('family_edit', args = (self.object.id,))

    def post(self, request, *args, **kwargs):
        if self.request.POST.get("confirm_delete"):
            # when confirmation page has been displayed and confirm button pressed
            queryset = super(FamilyDeleteView, self).get_queryset()
            queryset.filter(pk = self.kwargs['pk']).delete() # deleting on the queryset is more efficient than on the model object

            myid = self.kwargs['familyid']
            family_p = Family.objects.filter(familyid = myid).aggregate(sum = Sum('protein'))
            family_v = Family.objects.filter(familyid = myid).aggregate(sum = Sum('vita'))
            family_f = Family.objects.filter(familyid = myid).aggregate(sum = Sum('fe'))
            mydata = FamilyList.objects.get(id = myid).name
            rec = FamilyList.objects.filter(id = myid).first()
            rec.protein = family_p['sum']
            rec.vita = family_v['sum']
            rec.fe = family_f['sum']
            rec.save()
            return redirect('family_edit', familyid = myid)
        elif self.request.POST.get("cancel"):
            # when confirmation page has been displayed and cancel button pressed
            return redirect('family_edit', familyid = self.kwargs['familyid'])
        else:
            # when data is coming from the form which lists all items
            return self.get(self, *args, **kwargs)

class top_menu(LoginRequiredMixin, TemplateView):
    template_name = "app/topmenu.html"  # この行でテンプレート指定

class FamiliesAddView(LoginRequiredMixin, CreateView):
    model = FamilyList
    template_name = 'app/families_add.html'
    form_class = FamiliesAddForm

    def post(self, request, *args, **kwargs):
        if 'btn1' in request.POST:
            myname = request.POST.get('newfamily')
            FamilyList.objects.create(name = myname)
            myid =  FamilyList.objects.get(name = myname).id
            return redirect('family_edit', myid)

        return render(request, 'app/families_add.html', )


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
        if 'btn1' in request.POST:
            families = Families(data=request.POST)
            if families.is_valid():
                myid = FamilyList.objects.get(name = request.POST.get('familyname')).id
                return redirect('family_viewonly', familyid = myid)

        if 'btn2' in request.POST:
            myname = request.POST.get('newfamily')
            FamilyList.objects.create(name = myname)
            myid =  FamilyList.objects.get(name = myname).id
            return redirect('family_edit', myid)

    else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
        families = Families()

    return render(request, 'app/family_select.html', {
        'families' : families,
    })
