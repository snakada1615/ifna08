from django.views.generic import TemplateView, CreateView
from django.views.generic import ListView
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
from .models import FCT, Family, DRI, FamilyList
from .forms import Order_Key_Form, Families, Family_Create_Form


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
