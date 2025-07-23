from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [ #path aponta para a classe index dentro de views e isso se chamará index.
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]