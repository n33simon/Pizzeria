from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "PizzeriaApp"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("pizzas", views.pizzas, name="pizzas"),
    path("pizzas/<int:name_id>/", views.pizza, name="pizza"),
    path("comments/<int:name_id>/", views.comments, name="comments"),
    path("new_comment/<int:name_id>/", views.new_comment, name="new_comment"),
]
