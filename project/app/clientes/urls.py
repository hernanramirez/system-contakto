from app.clientes.api import ClienteTemplateView, ClienteUserViewSet
from app.clientes.views.solicitudes import (ClienteSolicitudCandidatoCreateView,
                                ClienteSolicitudCandidatoDeleteView,
                                ClienteSolicitudCandidatoUpdateView,
                                ClienteSolicitudCreateTemplateView,
                                ClienteSolicitudDeleteView,
                                ClienteSolicitudDetailView,
                                ClienteSolicitudEnviarTemplateView,
                                ClienteSolicitudListView, InitialClient,
                                MunicipiosView)
from app.clientes.views.clientes_users import (ClienteUserCreateView,
                                               ClienteUserDetailView,
                                               ClienteUserUpdatePasswdView,
                                               ClienteUserUpdateView)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clientes', ClienteUserViewSet)


app_name = "clientes"

urlpatterns = [

    path("api/", include(router.urls)),
    path("list/", ClienteTemplateView.as_view(), name="clientes_list"),

    path("user/create/", ClienteUserCreateView.as_view(), name="clientes_users_create"),
    path("user/detail/<int:pk>/", ClienteUserDetailView.as_view(), name="clientes_users_detail"),
    path("user/update/<int:pk>/", ClienteUserUpdateView.as_view(), name="clientes_users_update"),
    path("user/password/update/<int:pk>/", ClienteUserUpdatePasswdView.as_view(), name="clientes_users_password_update"),


    path('', InitialClient.as_view(), name='clientes_initial'),
    path('solicitudes/', ClienteSolicitudListView.as_view(), name='clientes_solicitudes_list'),
    path('solicitudes/create/', ClienteSolicitudCreateTemplateView.as_view(), name='clientes_solicitudes_create'),
    path('solicitudes/detail/<int:pk>/', ClienteSolicitudDetailView.as_view(), name='clientes_solicitud_detail'),
    path('solicitudes/delete/<int:pk>/', ClienteSolicitudDeleteView.as_view(), name='clientes_solicitud_delete'),
    path('solicitudes/enviar/<int:solicitud_id>/', ClienteSolicitudEnviarTemplateView.as_view(), name='clientes_solicitud_enviar'),

    path('solicitudes/candidato/create/<int:solicitud_id>/', ClienteSolicitudCandidatoCreateView.as_view(), name='clientes_solicitud_candidato_create'),
    path('solicitudes/candidato/update/<int:solicitud_id>/<int:pk>', ClienteSolicitudCandidatoUpdateView.as_view(), name='clientes_solicitud_candidato_update'),
    path('solicitudes/candidato/delete/<int:solicitud_id>/<int:pk>', ClienteSolicitudCandidatoDeleteView.as_view(), name='clientes_solicitud_candidato_delete'),
    
    path('municipios/<str:efe_key>/', MunicipiosView.as_view(), name='clientes_municipios'),
]
