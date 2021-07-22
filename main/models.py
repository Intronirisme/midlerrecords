from colorfield.fields import ColorField
from django.core.validators import FileExtensionValidator
from django.db import models
from polymorphic.models import PolymorphicModel

# Create your models here.

class Partenaire(models.Model):
    id = models.AutoField(primary_key=True,serialize=False, auto_created=True, unique=True)
    name = models.CharField(max_length=100, unique=True, verbose_name='nom')
    logo = models.ImageField(upload_to='partenaires/')
    url = models.URLField(verbose_name='lien vers le partenaire', null=True)

    def __str__(self):
        return '{0}'.format(self.name)

    class Meta:
        verbose_name = 'Partenaire'
        verbose_name_plural = 'Partenaires'


class Avantage(models.Model):
    id = models.AutoField(primary_key=True,serialize=False, auto_created=True, unique=True)
    text = models.CharField(max_length=100, null=False, verbose_name='avantage')

    def __str__(self):
        return '{0}'.format(self.text)

    class Meta:
        verbose_name = 'Avantage'
        verbose_name_plural = 'Avantages'


class Plugin(models.Model):
    id = models.AutoField(primary_key=True,serialize=False, auto_created=True, unique=True)
    name = models.CharField(max_length=100, unique=True, verbose_name='nom')
    icon = models.FileField(upload_to='plugins/', validators=[FileExtensionValidator( ['svg', 'jpg', 'png'] )], verbose_name='icône' )
    
    def __str__(self):
        return '{0}'.format(self.name)

    class Meta:
        verbose_name = 'Plugin'
        verbose_name_plural = 'Plugins'


class Page(PolymorphicModel):
    name = models.SlugField(max_length=100, unique=True, verbose_name='nom')
    color = ColorField(default='#ffffff')
    icon = models.FileField(upload_to='icons/', validators=[FileExtensionValidator( ['svg'] )], verbose_name='icône' ) #accept only svg
    top = models.ForeignKey('self', on_delete=models.RESTRICT, related_name='TOP', null=True, blank=True, verbose_name='page du dessus')
    left = models.ForeignKey('self', on_delete=models.RESTRICT, related_name='LEFT', null=True, blank=True, verbose_name='page de gauche')
    right = models.ForeignKey('self', on_delete=models.RESTRICT, related_name='RIGHT', null=True, blank=True, verbose_name='page de droite')
    bottom = models.ForeignKey('self', on_delete=models.RESTRICT, related_name='BOTTOM', null=True, blank=True, verbose_name='page du dessous')

    def __str__(self):
        return '{0}'.format(self.name)

    @property
    def class_name(self):
        return self.__class__.__name__


class Accueil(Page):
    titre = models.CharField(max_length=100, null=False, verbose_name='titre')
    presentation = models.TextField(max_length=512, null=False, verbose_name='texte de présentation')
    partenaires = models.ManyToManyField(Partenaire, blank=True, verbose_name='partenaires')

    class Meta:
        verbose_name = "Page d'accueil"
        verbose_name_plural = "Pages d'accueils"


class Prestation(Page):
    TARIF_TYPE = (
        ('(Prix de départ)', 'DEPART'),
        ('/ Heure', 'HEURE'),
        ('(Prix fixe)', 'FIXE')
    )
    titre = models.CharField(max_length=100, unique=True, null=False, verbose_name='titre')
    prix = models.PositiveSmallIntegerField(verbose_name='prix')
    tarif = models.CharField(max_length=50, choices=TARIF_TYPE, default='HEURE', verbose_name='tarification')
    description = models.TextField(max_length=256, null=False)
    avantages = models.ManyToManyField(Avantage, blank=True, verbose_name='avantages')

    class Meta:
        verbose_name = 'Page prestation'
        verbose_name_plural = 'Pages de prestations'


class Studio(Page):
    image1 = models.ImageField(upload_to='studio/', verbose_name='première image')
    image2 = models.ImageField(upload_to='studio/', verbose_name='seconde image')
    plugins = models.ManyToManyField(Plugin, blank=True, verbose_name='plugins')

    class Meta:
        verbose_name = 'Page studio'
        verbose_name_plural = 'Pages studios'


class Site(models.Model):
    id = models.AutoField(primary_key=True,serialize=False, auto_created=True, unique=True)
    description = models.CharField(max_length=160, blank=True, verbose_name='description du site (visible sur Google)')
    mailing_address = models.EmailField(max_length=150, blank=True, verbose_name='email de contact')
    background = ColorField(default='#dfa7a7')
    fonttitle =  models.FileField(upload_to='fonts/', validators=[FileExtensionValidator( ['otf', 'ttf'] )], verbose_name='police de titre' )
    fontbody =  models.FileField(upload_to='fonts/', validators=[FileExtensionValidator( ['otf', 'ttf'] )], verbose_name='police de corp (regular)' )
    fontbodylight =  models.FileField(upload_to='fonts/', validators=[FileExtensionValidator( ['otf', 'ttf'] )], verbose_name='police de corp (light)' )
    fontbodybold =  models.FileField(upload_to='fonts/', validators=[FileExtensionValidator( ['otf', 'ttf'] )], verbose_name='police de corp (bold)' )
    front = models.ForeignKey(Page, on_delete=models.RESTRICT, related_name='FRONT_HOME', null=True, blank=True, verbose_name='page de devant')
    back = models.ForeignKey(Page, on_delete=models.RESTRICT, related_name='BACK_HOME', null=True, blank=True, verbose_name='page du derrière')
    right = models.ForeignKey(Page, on_delete=models.RESTRICT, related_name='RIGHT_HOME', null=True, blank=True, verbose_name='page de droite')
    left = models.ForeignKey(Page, on_delete=models.RESTRICT, related_name='LEFT_HOME', null=True, blank=True, verbose_name='page de gauche')
    top = models.ForeignKey(Page, on_delete=models.RESTRICT, related_name='TOP_HOME', null=True, blank=True, verbose_name='page du dessus')
    bottom = models.ForeignKey(Page, on_delete=models.RESTRICT, related_name='BOTTOM_HOME', null=True, blank=True, verbose_name='page du dessous')

    def __str__(self):
        return "paramètres généraux"

    class Meta:
        default_permissions = ('change', 'view')
        verbose_name = 'Apparence générale'
        verbose_name_plural = 'Apparence générale'