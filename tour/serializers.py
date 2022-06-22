
import email
from rest_framework import serializers

from .models import MyUser,Region,Tour,Compra,CompraTour


####################TODO MOSTRAR TODOS LOS TOURS################################
class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['tour_foto1'] = instance.tour_foto1.url
        representation['tour_foto2'] = instance.tour_foto2.url
        representation['tour_foto3'] = instance.tour_foto3.url
        representation['tour_foto4'] = instance.tour_foto4.url
        representation['tour_foto5'] = instance.tour_foto5.url
        return representation
class TourDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['tour_foto1'] = instance.tour_foto1.url
        representation['tour_foto2'] = instance.tour_foto2.url
        representation['tour_foto3'] = instance.tour_foto3.url
        representation['tour_foto4'] = instance.tour_foto4.url
        representation['tour_foto5'] = instance.tour_foto5.url
        return representation
######################TODO MOSTRAR TOUR POR REGION###############################
class RegionTourSerializer(serializers.ModelSerializer):
    Tour = TourSerializer(many=True,read_only=True)
    class Meta:
        model = Region
        fields = ['region_id','region_nombre','Tour']
#######################TODO MOSTRAR TODOS LOS CLIENTES##################################
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['cliente_foto'] = instance.cliente_foto.url
        return representation  
    
######################TODO MOSTRAR TODAS LAS REGIONES#########################
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
#######################TODO MOSTRAR TODAS LAS COMPRAS############################
class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'


##################################TODO PARA HACER LA COMPRA#############################################
class CompraTourSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = CompraTour
        fields = ['tour_id','compratour_cantidad','tour_precio_oferta']
        


class CompraSerializerPOST(serializers.ModelSerializer):
    compratours = CompraTourSerializerPOST(many=True)
    class Meta:
        model = Compra
        fields = ['compra_fecha','compra_hora','compra_nro','user_id','estado','compratour_total','compratours',]
        
    def create(self, validated_data):
        compras_data = validated_data.pop('compratours')
        compra = Compra.objects.create(**validated_data)
        for compra_data in compras_data:
            CompraTour.objects.create(compra_id=compra,**compra_data)
        return compra
    
###############################TODO CREAR NUEVO USUARIO#######################################################



######################TODO OBTENER DETALLE DE COMPRA#######################################################
class TourSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['tour_nombre','tour_foto1']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['tour_foto1'] = instance.tour_foto1.url
        return representation 

class CompraTourSerializerGET(serializers.ModelSerializer):
    tour = TourSerializerGET(source='tour_id')
    class Meta:
        
        model = CompraTour
        fields = ['tour_id','compratour_cantidad','tour_precio_oferta','tour']
        
        
class CompraSerializerGET(serializers.ModelSerializer):
    compratours = CompraTourSerializerGET(many=True)
    class Meta:
        model = Compra
        fields = ['compra_id','compra_fecha','compra_nro','user_id','estado','compra_hora','compratour_total','compratours',]
        
        
class ClienteTourSerializer(serializers.ModelSerializer):
    Compra = CompraSerializerGET(many=True)
    class Meta:
        model = MyUser
        fields = ['Compra']
        
        
        
        
"""
{
            "compra_fecha": "2022-05-30",
            "compra_nro": "0111",
            "cliente_id": 1,
           "compratours":
           [{
           "tour_id":1,
          "compratour_cantidad":1
         }]
}

INSERTAR COMPRA
{
    "compra_fecha":"2022-02-02",
    "compra_nro":"0000001",
    "cliente_id":"1",
    "estado":"solicitado",
    "compratours":[{
        "tour_id":"1",
        "compratour_cantidad":"5",
        "compratour_total":"750"
    }]
    
    INGRESAR TOUR :

        {
       
            "nombre": "Paga desde S/ 89.50 por Full Day Paracas - Huacachina, Incluye NADA, NADITAAAAAAA",
            "descripcion": "RESUMEN Wish Viajes Perú S.A.C, somos una agencia de viajes autorizada por el MINCETUR. Trabajamos con profesionales del sector turismo, somos especialistas en full days,",
            "itinerario": "transporte turístico (Ida – Vuelta) Guía Oficial de Turismo Visita Paracas – Ica – Viñedo - Chincha Visita a la bahía de Paracas Avistamiento de lobos marinos, aves, etc. Visita ",
            "precio": 90,
            "foto": "https://cuponassets.cuponatic-latam.com/backendPe/uploads/imagenes_descuentos/100360/cd126a7d2b5e19da398d5f281875cc13f3f48354.XL2.jpg",
            "stock": 26,
            "fecha_inicio": "2022-08-15",
            "fecha_fin": "2022-08-11",
            "region_id": 3
        }


}

"""

##############################TODO CREAR USUSARIO####################################################

from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True)
    class Meta:
        model = MyUser
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['cliente_foto'] = instance.cliente_foto.url
        return representation 
    
    def create(self,validated_data):
        user=MyUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    