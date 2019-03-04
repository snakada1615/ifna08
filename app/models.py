from django.db import models

# Create your models here.

class FCT(models.Model):

    FCT_id = models.IntegerField(default=1)
    food_grp_id = models.IntegerField(default=1)
    food_item_id = models.IntegerField(default=1)
    Food_grp = models.CharField(max_length=200)
    Food_name = models.CharField(max_length=200)
    Crop_ref = models.CharField(max_length=200)
    Edible = models.FloatField(default=0)
    Energy = models.FloatField(default=0)
    WATER = models.FloatField(default=0)
    Protein = models.FloatField(default=0)
    Fat = models.FloatField(default=0)
    Carbohydrate = models.FloatField(default=0)
    Fiber = models.FloatField(default=0)
    ASH = models.FloatField(default=0)
    CA = models.FloatField(default=0)
    FE = models.FloatField(default=0)
    MG = models.FloatField(default=0)
    P = models.FloatField(default=0)
    K = models.FloatField(default=0)
    NA = models.FloatField(default=0)
    ZN = models.FloatField(default=0)
    CU = models.FloatField(default=0)
    VITA_RAE = models.FloatField(default=0)
    RETOL = models.FloatField(default=0)
    B_Cart_eq = models.FloatField(default=0)
    VITD = models.FloatField(default=0)
    VITE = models.FloatField(default=0)
    THIA = models.FloatField(default=0)
    RIBF = models.FloatField(default=0)
    NIA = models.FloatField(default=0)
    VITB6C = models.FloatField(default=0)
    FOL = models.FloatField(default=0)
    VITB12 = models.FloatField(default=0)
    VITC = models.FloatField(default=0)

    def __str__(self):
        return self.Food_name

class DRI(models.Model):

    age_id = models.IntegerField(default=1)
    male_protain = models.FloatField(default=0)
    male_vitA = models.FloatField(default=0)
    male_fe = models.FloatField(default=0)
    female_protain = models.FloatField(default=0)
    female_vitA = models.FloatField(default=0)
    female_fe = models.FloatField(default=0)

    def __str__(self):
        return self.age_id


class DRI_women(models.Model):

    status = models.CharField(max_length=200)
    female_prot2 = models.FloatField(default=0)
    female_vit2 = models.FloatField(default=0)
    female_fe2 = models.FloatField(default=0)

    def __str__(self):
        return self.status

class FamilyList(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=200,
    )
    protein = models.FloatField(
        verbose_name='protein',
        default=0
    )
    vita = models.FloatField(
        verbose_name='Vit-A',
        default=0
    )
    fe = models.FloatField(
        verbose_name='iron',
        default=0
    )
    def __str__(self):
        return self.name


class Family(models.Model):
    # bookid : INTEGER型で、主キー
    AGE_CHOICES = (
        (1, '0 <= age < 0.5'),
        (2, '0.5 <= age < 1'),
        (3, '1 <= age < 1.5'),
        (4, '1.5 <= age < 2'),
        (5, '2 <= age < 3'),
        (6, '3 <= age < 4'),
        (7, '4 <= age < 5'),
        (8, '5 <= age < 6'),
        (9, '6 <= age < 7'),
        (10, '7 <= age < 8'),
        (11, '8 <= age < 9'),
        (11, '9 <= age < 10'),
        (12, '10 <= age < 11'),
        (13, '11 <= age < 12'),
        (14, '12 <= age < 13'),
        (15, '13 <= age < 14'),
        (16, '14 <= age < 15'),
        (17, '15 <= age < 16'),
        (18, '16 <= age < 17'),
        (19, '17 <= age < 18'),
        (20, '18 <= age < 19'),
        (21, '19 <= age < 65'),
        (22, '65 <= age'),
    )

    SEX_CHOICES = (
        (1, 'male'),
        (2, 'female'),
    )

    WOMEN_SPECIAL = (
        (0, 'no'),
        (1, 'pregnancy first 3 month'),
        (2, 'pregnancy 4 to 6 month'),
        (3, 'pregnancy 7 to 9 month'),
        (4, 'lactation 0-6 month'),
        (5, 'lactation over 7 month'),
    )

    familyid = models.IntegerField(
        default=0,
    )

    name = models.CharField(
        verbose_name='name',
        max_length=200,
        default='no name'
    )

    age = models.IntegerField(
        verbose_name='age',
        choices=AGE_CHOICES,
        default=1,
    )

    sex = models.IntegerField(
        verbose_name='sex',
        choices=SEX_CHOICES,
        default=1,
    )

    women_s = models.IntegerField(
        verbose_name='women_special',
        choices=WOMEN_SPECIAL,
        default=0,
    )

    protein = models.FloatField(
        verbose_name='protein',
        default=0
    )

    vita = models.FloatField(
        verbose_name='Vit-A',
        default=0
    )

    fe = models.FloatField(
        verbose_name='iron',
        default=0
    )

    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Family information'
        verbose_name_plural = 'Family information'