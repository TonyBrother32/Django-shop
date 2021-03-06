from django import forms
from authnapp.forms import ShopUserEditForm
from authnapp.models import ShopUser
from mainapp.models import ProductCategory

class ShopUserAdminForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'


class ProductCategoryAdminForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
