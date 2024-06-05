from django import forms
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView,
    DetailView,
)

from buildings.forms import (
    DefaultLadderForm,
    DefaultPillarForm,
    DefaultPlateForm,
    MathForm,
    return_ladder_choices,
    return_pillar_choices,
    return_plate_choices,
)
from buildings.models import Building, Ladder, Pillar, Plate

# Create your views here.


class PillarListView(ListView):
    model = Pillar
    template_name = "buildings/pillar_list.html"


class PillarUpdateView(UpdateView):
    model = Pillar
    template_name = "buildings/pillar_form.html"
    success_url = reverse_lazy("buildings:pillar_list")
    form_class = DefaultPillarForm


class PillarCreateView(CreateView):
    model = Pillar
    template_name = "buildings/pillar_form.html"
    success_url = reverse_lazy("buildings:pillar_list")
    form_class = DefaultPillarForm


class PillarDeleteView(DeleteView):
    model = Pillar
    success_url = reverse_lazy("buildings:pillar_list")
    template_name = "buildings/pillar_delete.html"


class LadderListView(ListView):
    model = Ladder
    template_name = "buildings/ladder_list.html"


class LadderUpdateView(UpdateView):
    model = Ladder
    template_name = "buildings/ladder_form.html"
    success_url = reverse_lazy("buildings:ladder_list")
    form_class = DefaultLadderForm


class LadderCreateView(CreateView):
    model = Ladder
    template_name = "buildings/ladder_form.html"
    success_url = reverse_lazy("buildings:ladder_list")
    form_class = DefaultLadderForm


def check_with_other(data, object):
    flag = True
    if data["pillars_count"] != object.pillars_count:
        flag = False
    if data["plates_count"] != object.plates_count:
        flag = False
    if data["laddets_count"] != object.ladders_count:
        flag = False
    return flag


def check_math(data):
    pilars_count = int(
        data["width"]
        / data["x_step"]
        * data["length"]
        / data["y_step"]
        * data["floors"]
    )
    ladder_hole = 0
    ladders_count = 0
    if data["has_ladder"]:
        ladder = Ladder.objects.all()[int(data["ladder"]) - 1]
        ladder_hole = ladder.length * ladder.width
        ladders_count = (data["floors"] - 1) * 2
    plate = Plate.objects.all()[int(data["plate"]) - 1]
    plates_count = int(
        (
            data["length"] * data["width"]
            - data["elevator_length"] * data["elevator_width"]
            - ladder_hole
        )
        / (plate.length * plate.width)
        * data["floors"]
    )
    flag = True
    print(data)
    if data["pillars_count"] != pilars_count:
        flag = False
        print(pilars_count)
    if data["plates_count"] != plates_count:
        flag = False
        print(plates_count)
    if data["ladders_count"] != ladders_count:
        flag = False
        print(ladders_count)
        print("lestmicy")
    return flag


class LadderDeleteView(DeleteView):
    model = Ladder
    success_url = reverse_lazy("buildings:ladder_list")
    template_name = "buildings/ladder_delete.html"


class PlateListView(ListView):
    model = Plate
    template_name = "buildings/plate_list.html"


class PlateUpdateView(UpdateView):
    model = Plate
    template_name = "buildings/plate_form.html"
    success_url = reverse_lazy("buildings:plate_list")
    form_class = DefaultPlateForm


class PlateCreateView(CreateView):
    model = Plate
    template_name = "buildings/plate_form.html"
    success_url = reverse_lazy("buildings:plate_list")
    form_class = DefaultPlateForm


class PlateDeleteView(DeleteView):
    model = Plate
    success_url = reverse_lazy("buildings:plate_list")
    template_name = "buildings/plate_delete.html"


class BuildigListView(ListView):
    model = Building
    template_name = "buildings/building_list.html"


class BuildingDetailView(DetailView):
    model = Building
    template_name = "buildings/building_detail.html"


class BuildingDeleteView(DeleteView):
    model = Building
    template_name = "buildings/building_delete.html"
    success_url = reverse_lazy("buildings:building_list")


def calculate(request):
    if request.method == "GET":
        pillars = return_pillar_choices()
        plates = return_plate_choices()
        ladders = return_ladder_choices()
        data = {"pillars": pillars, "plates": plates, "ladders": ladders}
        form = MathForm(data)
        return render(request, "buildings/math.html", {"form": form})
    else:
        form = MathForm(request.POST)
        if form.is_valid():
            building = Building.objects.filter(name=form.cleaned_data["name"])
            if building.exists():
                building = building[0]
                res = check_with_other(form.cleaned_data, building)
                if res:
                    return render(
                        request,
                        "buildings/math.html",
                        {"form": form, "message": "Рассчеты верны"},
                    )
                else:
                    return render(
                        request,
                        "buildings/math.html",
                        {"form": form, "message": "Рассчеты не верны"},
                    )
            else:
                res = check_math(form.cleaned_data)
                if res:
                    tmp_pil = Pillar.objects.all()[int(form.cleaned_data["pillar"]) - 1]
                    tmp_plate = Plate.objects.all()[int(form.cleaned_data["plate"]) - 1]
                    tmp_ladder = None
                    if form.cleaned_data["has_ladder"]:
                        tmp_ladder = Ladder.objects.all()[
                            int(form.cleaned_data["ladder"]) - 1
                        ]
                    new_building = Building.objects.create(
                        name=form.cleaned_data["name"],
                        industrial=form.cleaned_data["industrial"],
                        pillar=tmp_pil,
                        pillars_count=form.cleaned_data["pillars_count"],
                        plate=tmp_plate,
                        plates_count=form.cleaned_data["plates_count"],
                        ladder=tmp_ladder,
                        ladders_count=form.cleaned_data["ladders_count"],
                        has_elevator=form.cleaned_data["has_elevator"],
                        elevator_length=form.cleaned_data["elevator_length"],
                        elevator_width=form.cleaned_data["elevator_width"],
                        x_step=form.cleaned_data["x_step"],
                        y_step=form.cleaned_data["y_step"],
                        floors=form.cleaned_data["floors"],
                        length=form.cleaned_data["length"],
                        width=form.cleaned_data["width"],
                        height=form.cleaned_data["height"],
                    )
                    new_building.save()
                    return redirect("buildings:building_list")
                else:
                    return render(
                        request,
                        "buildings/math.html",
                        {"form": form, "message": "Рассчеты не верны"},
                    )
        else:
            pillars = return_pillar_choices()
            plates = return_plate_choices()
            ladders = return_ladder_choices()
            form = MathForm(pillars=pillars, plates=plates, ladders=ladders)
            return render(request, "buildings/math.html", {"form": form})
