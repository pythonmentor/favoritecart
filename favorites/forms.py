from django import forms

from items.models import Item
from .models import Favorite


class SaveFavoriteForm(forms.Form):
    item = forms.IntegerField(widget=forms.HiddenInput(), required=True)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(request.POST, *args, **kwargs)

    def clean_item(self):
        item = self.cleaned_data.get('item')
        try:
            item = Item.objects.get(pk=item)
        except Item.DoesNotExist:
            raise forms.ValidationError(
                "The item you want to save does not exist"
            )
        return item

    def save(self, commit=True):
        item = self.cleaned_data.get("item")
        try:
            favorite = Favorite.objects.get(user=self.request.user, item=item)
        except Favorite.DoesNotExist:
            favorite = Favorite(user=self.request.user, item=item)
            if commit:
                favorite.save()
        return favorite
