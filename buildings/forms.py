from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList

from buildings.models import Ladder, Pillar, Plate


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class DefaultPillarForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Pillar
        fields = ("serial_number", "length", "width", "height")


class DefaultLadderForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Ladder
        fields = ("serial_number", "length", "width", "height")


def return_pillar_choices():
    pillar_names = []
    pillars = Pillar.objects.all()
    if pillars.exists():
        for pillar in pillars:
            pillar_names.append(pillar.serial_number)
    pillar_choices = ()
    counter = 1
    for name in pillar_names:
        tmp = (str(counter), name)
        pillar_choices = pillar_choices + (tmp,)
        counter += 1
    return pillar_choices


def return_plate_choices():
    plates = Plate.objects.all()
    plate_names = []
    if plates.exists():
        for plate in plates:
            plate_names.append(plate.serial_number)
    plate_choices = ()
    counter = 1
    for name in plate_names:
        tmp = (str(counter), name)
        plate_choices = plate_choices + (tmp,)
        counter += 1
    return plate_choices


def return_ladder_choices():
    ladders = Ladder.objects.all()
    ladder_names = []
    if ladders.exists():
        for ladder in ladders:
            ladder_names.append(ladder.serial_number)
    ladder_choices = ()
    counter = 1
    for name in ladder_names:
        tmp = (str(counter), name)
        ladder_choices = ladder_choices + (tmp,)
        counter += 1
    return ladder_choices


class MathForm(forms.Form):
    name = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={"class": "form-control", "required":True}),
        label="Наименование",
        required=False
    )
    industrial = forms.BooleanField(
        initial=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        label="Промышленное",
        required=False,
    )
    length = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={"class": "form-control", "required":True}),
        label="Длина",
        required=False
    )
    width = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={"class": "form-control", "required":True}),
        label="Ширина",
        required=False
    )
    height = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={"class": "form-control", "required":True}),
        label="Высота",
        required=False
    )
    pillar = forms.ChoiceField(
        choices=return_pillar_choices(),
        widget=forms.Select(attrs={"class": "form-select", "required":True}),
        label="Колонна",
        required=False
    )
    pillars_count = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={"class": "form-control", "required":True}),
        label="Количество колонн",
        required=False
    )
    plate = forms.ChoiceField(
        choices=return_plate_choices(),
        widget=forms.Select(attrs={"class": "form-select", "required":True}),
        label="Плита",
        required=False
    )
    plates_count = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={"class": "form-control", "required":True}),
        label="Количество плит",
        required=False
    )
    has_ladder = forms.BooleanField(
        initial=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        label="Лестницы",
        required=False,
    )
    has_elevator = forms.BooleanField(
        initial=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        label="Лифт",
        required=False,
    )
    elevator_length = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={"class": "form-control", "required":True}),
        label="Длина лифта, 0 если не используется",
        required=False
    )
    elevator_width = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={"class": "form-control", "required":True}),
        label="Ширина лифта, 0 если не используется",
        required=False
    )
    ladder = forms.ChoiceField(
        choices=return_ladder_choices(),
        widget=forms.Select(attrs={"class": "form-select", "required":True}),
        label="Лестница",
        required=False
    )
    ladders_count = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={"class": "form-control", "required":True}),
        label="Количество лестниц, 0 если не используется",
        required=False
    )
    x_step = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={"class": "form-control", "required":True}),
        label="Шаг по горизонтали",
        required=False
    )
    y_step = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={"class": "form-control", "required":True}),
        label="Шаг по вертикали",
        required=False
    )
    floors = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(attrs={"class": "form-control", "required":True}),
        label="Количество этажей",
        required=False
    )

    def __init__(
        self, *args, **kwargs
    ) -> None:
        super(MathForm, self).__init__(*args, **kwargs)
        pillars = kwargs.pop('pillars', None)
        plates = kwargs.pop('plates', None)
        ladders = kwargs.pop('ladders', None)
        if plates:
            self.fields["plate"].choices = plates
        if pillars:
            self.fields["pillar"].choices = pillars
        if ladders:
            self.fields["ladder"].choices = ladders


class DefaultPlateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Plate
        fields = ("serial_number", "length", "width", "height")
