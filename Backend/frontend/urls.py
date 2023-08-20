from django.urls import path
from . import views
urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('streamlit/', views.streamlit_view, name='streamlit_app'),

]