from django.urls import path
from buildings.apps import BuildingsConfig
from buildings.views import LadderCreateView, LadderDeleteView, LadderListView, LadderUpdateView, PillarCreateView, PillarDeleteView, PillarListView, PillarUpdateView, PlateCreateView, PlateDeleteView, PlateListView, PlateUpdateView


app_name = BuildingsConfig.name

urlpatterns = [
    path("pillar", PillarListView.as_view(), name="pillar_list"),
    path("pillar/<int:pk>/update", PillarUpdateView.as_view(), name="pillar_update"),
    path("pillar/create", PillarCreateView.as_view(), name="pillar_create"),
    path("pillar/<int:pk>/delete", PillarDeleteView.as_view(), name="pillar_delete"),
    path("ladder", LadderListView.as_view(), name="ladder_list"),
    path("ladder/<int:pk>/update", LadderUpdateView.as_view(), name="ladder_update"),
    path("ladder/create", LadderCreateView.as_view(), name="ladder_create"),
    path("ladder/<int:pk>/delete", LadderDeleteView.as_view(), name="ladder_delete"),
    path("plate", PlateListView.as_view(), name="plate_list"),
    path("plate/<int:pk>/update", PlateUpdateView.as_view(), name="plate_update"),
    path("plate/create", PlateCreateView.as_view(), name="plate_create"),
    path("plate/<int:pk>/delete", PlateDeleteView.as_view(), name="plate_delete"),
]