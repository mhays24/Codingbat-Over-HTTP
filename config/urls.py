from django.contrib import admin
from django.urls import path


from app.views import number_view, string_splosion_view, cat_dog_view, lone_sum_view


urlpatterns = [
    path("number/<int:n>/", number_view),
    path("string_splosion/<str:word>/", string_splosion_view),
    path("cat-dog/<str:animal>/", cat_dog_view),
    path("lone_sum/<int:a>/<int:b>/<int:c>/", lone_sum_view),
    path("admin/", admin.site.urls),
]
