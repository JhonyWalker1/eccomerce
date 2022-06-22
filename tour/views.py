from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

# Create your views here.

from .models import *

from .serializers import *

class IndexView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        context = {
            'ok':True,
            'message':'Bienvenido a la API de Tours'
        }
        return Response(context)


######################TODO SOBRE REGION########################
class RegionView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        dataRegion = Region.objects.all()
        serRegion = RegionSerializer(dataRegion,many=True)
        context = {
            'ok':True,
            'content':serRegion.data
        }
        return Response(context)

###############TODO SOBRE CLIENTE ######################
class ClienteView(APIView):
    """ permission_classes = (IsAuthenticated,) """
    def get(self,request):
        dataCliente = MyUser.objects.all()
        serCliente = ClienteSerializer(dataCliente,many=True)
        context = {
            'ok':True,
            'content':serCliente.data
        }
        return Response(context)
            
class DetalleClienteView(APIView):
    def get(self,request,user_id):
        try:
            dataCliente = MyUser.objects.get(pk=user_id)
            serCliente = ClienteSerializer(dataCliente)
            context = {
                'ok':True,
                'content':serCliente.data
            }
        except MyUser.DoesNotExist:
            context = {
                'ok':False,
                'message':'Cliente no existe'
            }
        return Response(context)
    
class ClienteTourView(APIView):
    def get(self,request,id):
        dataCliente = MyUser.objects.get(pk=id)
        serClienteTour = ClienteTourSerializer(dataCliente)
        context = {
            'ok':True,
            'content':serClienteTour.data
        }
        return Response(context)
    
############TODO SOBRE TOUR############################
class TourView(APIView):
    """ permission_classes = (IsAuthenticated,) """
    def get(self,request):
        dataTour = Tour.objects.all()
        serTour = TourSerializer(dataTour,many=True)
        context = {
            'ok':True,
            'content':serTour.data
        }
        return Response(context)
    
class TourDetalleView(APIView):
    def get(self,request,tour_id):
        dataDetalleTour = Tour.objects.get(pk=tour_id)
        serDetalleTour = TourSerializer(dataDetalleTour)
        context = {
            'ok':True,
            'content':serDetalleTour.data
        }
        return Response(context)


class RegionTourView(APIView):
 
    def get(self,request,region_id):
        dataRegion = Region.objects.get(pk=region_id)
        print (dataRegion)
        serRegionTour = RegionTourSerializer(dataRegion)
        context = {
            'ok':True,
            'content':serRegionTour.data
        }
        return Response(context)
    
##############TODO SOBRE COMPRA############################

from django.db.transaction import atomic

class CompraView(APIView):
    """ permission_classes = (IsAuthenticated,) """
    def get(self,request):
        dataCompra = Compra.objects.all()
        serCompra = CompraSerializerGET(dataCompra,many=True)
        context = {
            'ok':True,
            'content':serCompra.data
        }
        return Response(context)
    @atomic
    def post(self,request):
        serCompra = CompraSerializerPOST(data=request.data)
        serCompra.is_valid(raise_exception=True)
        serCompra.save()
        
        context = {
            'ok':True,
            'content':serCompra.data
        }
        return Response(context)
    
    
#############TODO CREAR NUEVO USUARIO##########################


class UsuarioCreateView(APIView):
    def post(self,request):
        serUsuario = ClienteSerializer(data=request.data)
        serUsuario.is_valid(raise_exception=True)
        serUsuario.save()
        context = {
            'ok':True,
            'content':serUsuario.data
        }
        return Response(context)
    
    def get(self,request):
        dataUsuario = MyUser.objects.all()
        serUsuario = ClienteSerializer(dataUsuario,many=True)
        context = {
            'ok':True,
            'content':serUsuario.data
        }
        return Response(context)
    

from rest_framework import generics
from cloudinary.uploader import upload

class RegistrerView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = MyUser.objects.all()
    
class ImagenProfileView(APIView):
    def post(self,request):
        #upload image to cloudinary with django
        image = request.data.get('image')
        cloudinaryData = upload(image,folder="imgprofile")
        context = {
            'ok':True,
            'content':cloudinaryData
        }
        return Response(context)
        
       
        
    
    
    

     

    
    