from django import forms
from .models import Product

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 🎨 стилизация
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

        # чекбокс отдельно
        if "is_published" in self.fields:
            self.fields["is_published"].widget.attrs.update({"class": "form-check-input"})

    # 🚫 запрещённые слова (title)
    def clean_name(self):
        name = self.cleaned_data.get("name")
        self._validate_forbidden_words(name)
        return name

    # 🚫 запрещённые слова (description)
    def clean_description(self):
        description = self.cleaned_data.get("description")
        self._validate_forbidden_words(description)
        return description

    def _validate_forbidden_words(self, text):
        if text:
            for word in FORBIDDEN_WORDS:
                if word.lower() in text.lower():
                    raise forms.ValidationError(
                        f"Запрещено использовать слово: {word}"
                    )

    # 💰 цена
    def clean_price(self):
        price = self.cleaned_data.get("price")

        if price is not None and price < 0:
            raise forms.ValidationError(
                "Цена не может быть отрицательной"
            )

        return price

    # 🖼 доп задание — изображение
    def clean_image(self):
        image = self.cleaned_data.get("image")

        if image:
            # размер
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError("Размер изображения не более 5MB")

            # формат
            if not image.content_type in ["image/jpeg", "image/png"]:
                raise forms.ValidationError("Допустимы только JPEG и PNG")

        return image
