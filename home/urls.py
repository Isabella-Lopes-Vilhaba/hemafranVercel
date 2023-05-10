from django.urls import path, include
from django.views.generic import TemplateView
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('ajax/', include([
        path('protetor-estribo', TemplateView.as_view(
            template_name='home/ajax/protetor-estribo.html'), name='protetor-estribo'),
        path('protetor-janela', TemplateView.as_view(
            template_name='home/ajax/protetor-janela.html'), name='protetor-janela'),
        path('acessorios-rastreador', TemplateView.as_view(
            template_name='home/ajax/acessorios-rastreador.html'), name='acessorios-rastreador'),
        path('t4s-rastreador', TemplateView.as_view(
            template_name='home/ajax/t4s-rastreador.html'), name='t4s-rastreador'),
        path('onixsat-rastreador', TemplateView.as_view(
            template_name='home/ajax/onixsat-rastreador.html'), name='onixsat-rastreador'),
        path('autotrac-rastreador', TemplateView.as_view(
            template_name='home/ajax/autotrac-rastreador.html'), name='autotrac-rastreador'),
        path('carroceria-bau', TemplateView.as_view(
            template_name='home/ajax/carroceria-bau.html'), name='carroceria-bau'),
        path('carroceria-sider', TemplateView.as_view(
            template_name='home/ajax/carroceria-sider.html'), name='carroceria-sider'),
        path('carroceria-aberta', TemplateView.as_view(
            template_name='home/ajax/carroceria-aberta.html'), name='carroceria-aberta'),
        path('seguros-apolices', TemplateView.as_view(
            template_name='home/ajax/seguros-apolices.html'), name='seguros-apolices'),
        path('seguros-gr', TemplateView.as_view(
            template_name='home/ajax/seguros-gr.html'), name='seguros-gr'),
        path('seguros-adicionais', TemplateView.as_view(
            template_name='home/ajax/seguros-adicionais.html'), name='seguros-adicionais'),
    ])),
]
