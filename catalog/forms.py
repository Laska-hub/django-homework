from django import forms
from .models import Product


FORBIDDEN_WORDS = [
    "казино", "криптовалюта", "крипта",
    "биржа", "дешево", "бесплатно",
    "обман", "полиция", "радар",
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["owner"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

        if "is_published" in self.fields:
            self.fields["is_published"].widget.attrs.update(
                {"class": "form-check-input"}
            )

    def clean_name(self):
        return self._validate(self.cleaned_data.get("name"))

    def clean_description(self):
        return self._validate(self.cleaned_data.get("description"))

    def _validate(self, text):
        if text:
            for word in FORBIDDEN_WORDS:
                if word in text.lower():
                    raise forms.ValidationError(f"Запрещено слово: {word}")
        return text

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")
        return price
