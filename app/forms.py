from django import forms
from django.contrib.admin import widgets
from .models import FamilyList, Family, DRI, DRI_women, Diet, FCT

import os

CHOICE = {
    ('0','food name'),
    ('1','protein'),
    ('2','iron'),
    ('3','Vitamine-A'),
}



class FamilyForm(forms.ModelForm):

    class Meta:
        model = Family
        fields = ('name','age','sex','women_s')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'ex.) Yamada family'}),
                    'age': forms.Select(),
                    'sex': forms.RadioSelect(),
                    'women_s': forms.RadioSelect(),
                  }

class BS4RadioSelect(forms.RadioSelect):
    input_type = 'radio'
    template_name = 'app/widgets/bs4_radio.html'

class Order_Key_Form(forms.Form):
    key1 = forms.ChoiceField(
        label='Order_key',
        widget=BS4RadioSelect,
#        widget=forms.RadioSelect(attrs={'label class': 'radio-inline'}),
        choices= CHOICE,
        initial=1,
        )

class FamiliesAddForm(forms.ModelForm):
    class Meta:
        model = FamilyList
        fields = ("name",)

class DietForm(forms.ModelForm):

    class Meta:
        model = Diet
        fields = ("familyid", "diet_type", "food_item_id", "Food_name", "food_wt")
        widgets = {
            'familyid': forms.HiddenInput(),
            'food_item_id': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        self.myid = kwargs.pop('familyid')
        super(DietForm, self).__init__(*args, **kwargs)
        myquery = FCT.objects.all()
        self.fields['Food_name'] = forms.ModelChoiceField(queryset=myquery, empty_label='select food', to_field_name='Food_name')

    def clean(self):
        cleaned_data = super(DietForm, self).clean()
        self.cleaned_data['food_item_id'] = FCT.objects.get(Food_name = self.cleaned_data['Food_name']).food_item_id
        self.cleaned_data['familyid'] = self.myid
        return cleaned_data



class Families(forms.Form):
    myquery = FamilyList.objects.all()
    fields = ('name')
    familyname = forms.ModelChoiceField(label='', queryset=myquery, empty_label='select name', to_field_name='name')

class Family_Create_Form(forms.ModelForm):
    class Meta:
        model = Family
        fields = ("familyid", "name" ,"age", "sex", "women_s", "protein", "vita", "fe")
        widgets = {'name': forms.HiddenInput(),'familyid': forms.HiddenInput(),'protein': forms.HiddenInput(), 'vita': forms.HiddenInput(), 'fe': forms.HiddenInput()}

    def clean_women_s(self):
        a = self.cleaned_data['women_s']
        if self.cleaned_data['sex'] == 1:
            a = 0
        women_s = a
        return women_s

    def clean_protein(self):
        a = int(self.cleaned_data['age'])
        b = int(self.cleaned_data['women_s'])
        v1 = DRI.objects.get(age_id = a)
        if self.cleaned_data['sex'] == 1:
            protein = v1.male_protain
        else:
            try:
                v2 = DRI_women.objects.get(status = b)
                protein = v1.female_protain + v2.female_prot2
            except:
                protein = v1.female_protain
        return protein

    def clean_vita(self):
        a = int(self.cleaned_data['age'])
        b = int(self.cleaned_data['women_s'])
        v1 = DRI.objects.get(age_id = a)
        if self.cleaned_data['sex'] == 1:
            vita = v1.male_vitA
        else:
            try:
                v2 = DRI_women.objects.get(status = b)
                vita = v2.female_vit2
            except:
                vita = v1.female_vitA
        return vita

    def clean_fe(self):
        a = int(self.cleaned_data['age'])
        b = int(self.cleaned_data['women_s'])
        v1 = DRI.objects.get(age_id = a)
        if self.cleaned_data['sex'] == 1:
            fe = v1.male_fe
        else:
            try:
                v2 = DRI_women.objects.get(status = b)
                if v2.female_fe2 == 0:
                    fe = v1.female_fe
                else:
                    fe = v2.female_fe2
            except:
                fe = v1.female_fe
        return fe
