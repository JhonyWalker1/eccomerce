from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),    
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    cliente_nombre= models.CharField(max_length=100)
    cliente_apellido = models.CharField(max_length=100)
    cliente_telefono = models.CharField(max_length=100)
    cliente_direccion = models.CharField(max_length=100)
    cliente_pais = models.CharField(max_length=100)
    cliente_ciudad = models.CharField(max_length=100)
    cliente_fecha_nacimiento = models.DateField(null=True, blank=True)
    cliente_foto = CloudinaryField('image')

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



###########################################################################################

""" class Cliente(models.Model):
    cliente_id=models.AutoField(primary_key=True)
    usuario_id = models.OneToOneField(User,related_name='Cliente',on_delete=models.RESTRICT)
    cliente_nombre = models.CharField(max_length=100)
    cliente_apellido = models.CharField(max_length=100)
    cliente_email = models.EmailField()
    cliente_telefono = models.CharField(max_length=100)
    cliente_direccion = models.CharField(max_length=100)
    cliente_pais = models.CharField(max_length=100)
    cliente_ciudad = models.CharField(max_length=100)
    cliente_fecha_nacimiento = models.DateField()
    cliente_foto = CloudinaryField('image')

    def __str__(self):
        return self.cliente_nombre """

class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.region_nombre

class Tour(models.Model):
    tour_id = models.AutoField(primary_key=True)
    tour_nombre = models.CharField(max_length=100)
    tour_descripcion = models.TextField()
    tour_itinerario1 = models.TextField()
    tour_itinerario2 = models.TextField(null=True, blank=True)
    tour_itinerario3 = models.TextField(null=True, blank=True)
    tour_itinerario4 = models.TextField(null=True, blank=True)
    tour_itinerario5 = models.TextField(null=True, blank=True)
    tour_incluye = models.TextField(null=True, blank=True)
    tour_noincluye = models.TextField(null=True, blank=True)
    tour_recomendaciones= models.TextField(null=True, blank=True)
    tour_restaurante = models.TextField(null=True, blank=True)
    tour_atractivos =models.TextField(null=True, blank=True)
    tour_precio = models.DecimalField(max_digits=10,decimal_places=2,default=0,
                                    verbose_name='precio')
    tour_precio_oferta = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    tour_foto1 = CloudinaryField('image1')
    tour_foto2 = CloudinaryField('image2',null=True, blank=True)
    tour_foto3 = CloudinaryField('image3',null=True, blank=True)
    tour_foto4 = CloudinaryField('image4',null=True, blank=True)
    tour_foto5 = CloudinaryField('image5',null=True, blank=True)
    region_id = models.ForeignKey(Region, on_delete=models.RESTRICT,related_name='Tour',
                                  to_field='region_id',db_column='region_id',verbose_name='region')
    tour_stock = models.IntegerField(default=0)
    tour_fecha_inicio = models.DateField()
    tour_fecha_fin = models.DateField()
    
    def __str__(self):
        return self.tour_nombre
    
class Compra(models.Model):
    compra_id = models.AutoField(primary_key=True)
    compra_fecha = models.DateField()
    compra_hora = models.TimeField()
    user_id = models.ForeignKey(MyUser, on_delete=models.RESTRICT,related_name='Compra',
                                  to_field='id',db_column='user_id',verbose_name='cliente')
    
    estado = models.CharField(max_length=20,default='Solicitado')
    compra_nro = models.CharField(max_length=100,default='',verbose_name='Nro Pedido')
    compratour_total = models.DecimalField(max_digits=10,decimal_places=2,default=0,
                                    verbose_name='total')
    
class CompraTour(models.Model):
    compratour_id = models.AutoField(primary_key=True)
    compra_id = models.ForeignKey(Compra, related_name='compratours',to_field='compra_id',
                                  on_delete=models.RESTRICT,db_column='compra_id',verbose_name='Compra')
    tour_id = models.ForeignKey(Tour, related_name='compratours',to_field='tour_id',
                                on_delete=models.RESTRICT,db_column='tour_id',verbose_name='Tour')
    compratour_cantidad = models.IntegerField(default=1)
    tour_precio_oferta = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    
    