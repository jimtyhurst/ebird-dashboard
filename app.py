import htmltools
from shiny import reactive, render
from shiny.express import input, ui
import sightings
import mapper


def build_species_choice_list(species: list) -> dict:
    choice_list = {}
    for item in species:
        choice_list[item] = item
    return choice_list


species_choices = build_species_choice_list(sightings.SPECIES_LIST)

ui.input_select("selected_species", "Choose one species", choices=list(species_choices.keys()))


@render.ui
def map():
    return htmltools.Tag(species_map()._repr_html_())


@reactive.calc
def species_map():
    selected_species = species_choices[input.selected_species()]
    return mapper.build_map(selected_species)
