from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect

from favoritecart.helpers import redirect_to_login
from favoritecart.cart import FavoriteCart
from .forms import SaveFavoriteForm


class SaveFavoriteView(View):
    """View responsible to handle the Favorite saving process."""

    def post(self, request):
        form = SaveFavoriteForm(request)
        if form.is_valid():
            return self.form_valid(form)

    def form_valid(self, form):
        item = form.cleaned_data['item']
        print("Authenticated? ", self.request.user)
        if not self.request.user.is_authenticated:
            cart = FavoriteCart(self.request)
            cart.add({"item": item.id, "user": "user"})
            return redirect_to_login(self.request)
        form.save(self.request)
        return redirect("pages:home")
