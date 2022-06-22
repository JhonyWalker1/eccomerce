from django.urls import path



from . import views

app_name = 'tour'

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('get-all-regions',views.RegionView.as_view()),
    path('get-all-tours',views.TourView.as_view()),
    path('tourdetalle/<int:tour_id>',views.TourDetalleView.as_view()),
    path('region/<int:region_id>/tour',views.RegionTourView.as_view()),
    path('cliente',views.ClienteView.as_view()),
    path('clientedetalle/<int:user_id>',views.DetalleClienteView.as_view()),
    path('cliente/<int:id>/compra',views.ClienteTourView.as_view()),
    path('compra',views.CompraView.as_view()),
    path('registrousuario',views.RegistrerView.as_view()),
    path('usuarioimageprofile',views.ImagenProfileView.as_view()),
]