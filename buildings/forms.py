from django import forms

from buildings.models import Ladder, Pillar, Plate

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class DefaultPillarForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Pillar
        fields = ("serial_number", "length", "width", "height")

class DefaultLadderForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Ladder
        fields = ("serial_number", "length", "width", "height")

class DefaultPlateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Plate
        fields = ("serial_number", "length", "width", "height")
    