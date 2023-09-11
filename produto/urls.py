from django.urls import path
from . import views

app_name = 'produto'
urlpatterns = [
    path('', views.ListaProdutos. as_view(),"lista"),
    path('<slug>', views.DetalheProduto. as_view(),"detalhe"),
    path('adicionaraocarrinho/', views.AdicionarAoCarrinho. as_view(),"adicionaraocarrinho"),
    path('removerdocarrinho/', views.RemoverDoCarrinho. as_view(),"removerdocarrinho"),
    path('carrinho/', views.Carrinho. as_view(),"carrinho"),
    path('finalizar/', views.Finalizar. as_view(),"finalizar"),
    
    
]