from django.urls import path
from .views import the_forecast_view

# /weather-forecat/<str: for_date>/<str: country_code>/
urlpatterns = [
    path('<str:for_date>/<str:country_code>/', the_forecast_view, name="get_forecast"),
]
