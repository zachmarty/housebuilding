from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from buildings.forms import DefaultLadderForm, DefaultPillarForm, DefaultPlateForm
from buildings.models import Ladder, Pillar, Plate
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