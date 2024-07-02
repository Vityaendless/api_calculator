from django.urls import path

from .views import IndexView, AddView, SubtractView, MultiplyView, DivideView


app_name = 'webapp'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', AddView.as_view(), name='add'),
    path('subtract/', SubtractView.as_view(), name='subtract'),
    path('multiply/', MultiplyView.as_view(), name='multiply'),
    path('divide/', DivideView.as_view(), name='divide'),
]
