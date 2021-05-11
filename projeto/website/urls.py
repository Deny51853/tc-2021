from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('automatosFinitos/', views.automatosFinitos, name='automatosFinitos'),
    path('novoAutomato/', views.novoAutomato, name='novoAutomato'),
    path('<int:automato_id>/detalhesAutomato/', views.detalhesAutomato, name='detalhesAutomato'),
    path('editarAutomato/<int:automato_id>', views.editarAutomato, name='editarAutomato'),
    path('apagarAutomato/<int:automato_id>', views.apagarAutomato, name='apagarAutomato'),
    path('expressoesRegulares/', views.expressoesRegulares, name='expressoesRegulares'),
    path('novaExpressao/', views.novaExpressao, name='novaExpressao'),
    path('<int:expressao_id>/detalhesExpressao/', views.detalhesExpressao, name='detalhesExpressao'),
    path('editarExpressao/<int:expressao_id>', views.editarExpressao, name='editarExpressao'),
    path('apagarExpressao/<int:expressao_id>', views.apagarExpressao, name='apagarExpressao'),
    path('maquinasTuring/', views.maquinasTuring, name='maquinasTuring'),
    path('novaMaquina/', views.novaMaquina, name='novaMaquina'),
    path('<int:maquina_id>/detalhesMaquina/', views.detalhesMaquina, name='detalhesMaquina'),
    path('editarMaquina/<int:maquina_id>', views.editarMaquina, name='editarMaquina'),
    path('apagarMaquina/<int:maquina_id>', views.apagarMaquina, name='apagarMaquina')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)