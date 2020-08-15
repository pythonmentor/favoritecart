from django.urls import path

from .views import SaveFavoriteView

app_name = "favorites"

urlpatterns = [path('save/', SaveFavoriteView.as_view(), name="save")]
