import email
from email import message
#from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.forms import ValidationError
from django.utils import timezone
from time import timezone
from django.contrib.admin.widgets import AdminDateWidget
# from django.conf import settings.User
#from .widgets import BootstrapDateTimePickerInput
from platformdirs import user_config_dir
from PIL import Image


class User(AbstractUser):

    WILAYA_CHOICES = (
        (0, 'Wilaya'),
        (1, '1- ADRAR'),
        (2, '2- CHLEF'),
        (3, '3 - LAGHOUAT'),
        (4, '4 - OUM BOUAGHI'),
        (5, '5 - BATNA'),
        (6, '6 - BEJAIA'),
        (7, '7 - BISKRA'),
        (8, '8 - BECHAR'),
        (9, '9 - BLIDA'),
        (10, '10 - BOUIRA'),
        (11, '11 - TAMANRASSET'),
        (12, '12 - TEBESSA'),
        (13, '13 - TLEMCEN'),
        (14, '14 - TIARET'),
        (15, '15 - TIZI OUZOU'),
        (16, '16 - ALGER'),
        (17, '17 - DJELFA'),
        (18, '18 - JIJEL'),
        (19, '19 - SETIF'),
        (20, '20 - SAIDA'),
        (21, '21 - SKIKDA'),
        (22, '22 - SIDI BEL ABBES'),
        (23, '23 - ANNABA'),
        (24, '24 - GUELMA'),
        (25, '25 - CONSTANTINE'),
        (26, '26 - MEDEA'),
        (27, '27 - MOSTAGANEM'),
        (28, '28 - M\'SILA'),
        (29, '29 - MASCARA'),
        (30, '30 - OUARGLA'),
        (31, '31 - ORAN'),
        (32, '32 - EL BAYDH'),
        (33, '33 - ILLIZI'),
        (34, '34 - BORDJ BOU ARRERIDJ'),
        (35, '35 - BOUMERDES'),
        (36, '36 - EL TAREF'),
        (37, '37 - TINDOUF'),
        (38, '38 - TISSEMSILT'),
        (39, '39 - EL OUED'),
        (40, '40 - KHENCHLA'),
        (41, '41 - SOUK AHRASS'),
        (42, '42 - TIPAZA'),
        (43, '43 - MILA4'),
        (44, '44 - AÏN DEFLA'),
        (45, '45 - NÂAMA'),
        (46, '46 - AÏN TEMOUCHENT'),
        (47, '47 - GHARDAÏA'),
        (48, '48 - RELIZANE'),
        (49, '49 -Timimoun'),
        (50, '50-Bordj Badji Mokhtar'),
        (51, '51-Ouled Djellal'),
        (52, '52-Béni Abbès'),
        (53, '53-In Salah'),
        (54, '54-In Guezzam'),
        (55, '55-Touggourt'),
        (56, '56-Djanet'),
        (57, '57-M\'Ghair'),
        (58, '58-El Meniaa'),

    )
    wilaya = models.IntegerField(choices=WILAYA_CHOICES, default=0)
    email = models.EmailField(max_length=254)
    is_org = models.BooleanField(default=False)
    org_document = models.ImageField(
        upload_to='images/', null=True, blank=True)

    def clean(self):
        if self.is_org and not self.org_document:
            raise ValidationError("Organisation document is required.")
        elif self.is_org == False:
            self.org_document = None


class UserPost(models.Model):
    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    WILAYA_CHOICES = (
        (0, 'Wilaya'),
        (1, '1- ADRAR'),
        (2, '2- CHLEF'),
        (3, '3 - LAGHOUAT'),
        (4, '4 - OUM BOUAGHI'),
        (5, '5 - BATNA'),
        (6, '6 - BEJAIA'),
        (7, '7 - BISKRA'),
        (8, '8 - BECHAR'),
        (9, '9 - BLIDA'),
        (10, '10 - BOUIRA'),
        (11, '11 - TAMANRASSET'),
        (12, '12 - TEBESSA'),
        (13, '13 - TLEMCEN'),
        (14, '14 - TIARET'),
        (15, '15 - TIZI OUZOU'),
        (16, '16 - ALGER'),
        (17, '17 - DJELFA'),
        (18, '18 - JIJEL'),
        (19, '19 - SETIF'),
        (20, '20 - SAIDA'),
        (21, '21 - SKIKDA'),
        (22, '22 - SIDI BEL ABBES'),
        (23, '23 - ANNABA'),
        (24, '24 - GUELMA'),
        (25, '25 - CONSTANTINE'),
        (26, '26 - MEDEA'),
        (27, '27 - MOSTAGANEM'),
        (28, '28 - M\'SILA'),
        (29, '29 - MASCARA'),
        (30, '30 - OUARGLA'),
        (31, '31 - ORAN'),
        (32, '32 - EL BAYDH'),
        (33, '33 - ILLIZI'),
        (34, '34 - BORDJ BOU ARRERIDJ'),
        (35, '35 - BOUMERDES'),
        (36, '36 - EL TAREF'),
        (37, '37 - TINDOUF'),
        (38, '38 - TISSEMSILT'),
        (39, '39 - EL OUED'),
        (40, '40 - KHENCHLA'),
        (41, '41 - SOUK AHRASS'),
        (42, '42 - TIPAZA'),
        (43, '43 - MILA4'),
        (44, '44 - AÏN DEFLA'),
        (45, '45 - NÂAMA'),
        (46, '46 - AÏN TEMOUCHENT'),
        (47, '47 - GHARDAÏA'),
        (48, '48 - RELIZANE'),
        (49, '49 -Timimoun'),
        (50, '50-Bordj Badji Mokhtar'),
        (51, '51-Ouled Djellal'),
        (52, '52-Béni Abbès'),
        (53, '53-In Salah'),
        (54, '54-In Guezzam'),
        (55, '55-Touggourt'),
        (56, '56-Djanet'),
        (57, '57-M\'Ghair'),
        (58, '58-El Meniaa'),

    )
    wilaya = models.IntegerField(choices=WILAYA_CHOICES, default=0)

    def __str__(self):
        return self.title


class Event(models.Model):
    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField(null=True)
    participated = models.ManyToManyField(
        User, default=None, blank=True, related_name='participated')
    WILAYA_CHOICES = (
        (0, 'Wilaya'),
        (1, '1- ADRAR'),
        (2, '2- CHLEF'),
        (3, '3 - LAGHOUAT'),
        (4, '4 - OUM BOUAGHI'),
        (5, '5 - BATNA'),
        (6, '6 - BEJAIA'),
        (7, '7 - BISKRA'),
        (8, '8 - BECHAR'),
        (9, '9 - BLIDA'),
        (10, '10 - BOUIRA'),
        (11, '11 - TAMANRASSET'),
        (12, '12 - TEBESSA'),
        (13, '13 - TLEMCEN'),
        (14, '14 - TIARET'),
        (15, '15 - TIZI OUZOU'),
        (16, '16 - ALGER'),
        (17, '17 - DJELFA'),
        (18, '18 - JIJEL'),
        (19, '19 - SETIF'),
        (20, '20 - SAIDA'),
        (21, '21 - SKIKDA'),
        (22, '22 - SIDI BEL ABBES'),
        (23, '23 - ANNABA'),
        (24, '24 - GUELMA'),
        (25, '25 - CONSTANTINE'),
        (26, '26 - MEDEA'),
        (27, '27 - MOSTAGANEM'),
        (28, '28 - M\'SILA'),
        (29, '29 - MASCARA'),
        (30, '30 - OUARGLA'),
        (31, '31 - ORAN'),
        (32, '32 - EL BAYDH'),
        (33, '33 - ILLIZI'),
        (34, '34 - BORDJ BOU ARRERIDJ'),
        (35, '35 - BOUMERDES'),
        (36, '36 - EL TAREF'),
        (37, '37 - TINDOUF'),
        (38, '38 - TISSEMSILT'),
        (39, '39 - EL OUED'),
        (40, '40 - KHENCHLA'),
        (41, '41 - SOUK AHRASS'),
        (42, '42 - TIPAZA'),
        (43, '43 - MILA4'),
        (44, '44 - AÏN DEFLA'),
        (45, '45 - NÂAMA'),
        (46, '46 - AÏN TEMOUCHENT'),
        (47, '47 - GHARDAÏA'),
        (48, '48 - RELIZANE'),
        (49, '49 -Timimoun'),
        (50, '50-Bordj Badji Mokhtar'),
        (51, '51-Ouled Djellal'),
        (52, '52-Béni Abbès'),
        (53, '53-In Salah'),
        (54, '54-In Guezzam'),
        (55, '55-Touggourt'),
        (56, '56-Djanet'),
        (57, '57-M\'Ghair'),
        (58, '58-El Meniaa'),

    )
    wilaya = models.IntegerField(choices=WILAYA_CHOICES, default=0)

    def __str__(self):
        return self.title

    @property
    def num_participate(self):
        return self.participated.all().count()


class Participate(models.Model):
    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    PARICIPATE_CHOICES = (
        ('Participate', 'Participate'),
        ('Unparticipate', 'Unparticipate')
    )
    value = models.CharField(choices=PARICIPATE_CHOICES,
                             default='Participate', max_length=50)

    def __str__(self):
        return str(self.event)


class Profile(models.Model):
    User = settings.AUTH_USER_MODEL
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='pofile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'




class ContactUs(models.Model):
    message_name=models.CharField(max_length=50)
    message_email=models.EmailField(max_length=60)
    message=models.TextField(max_length=2000)

    def __str__(self):
       return str(self.message_name)

