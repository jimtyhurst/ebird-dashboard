from pathlib import Path
import htmltools
from shiny import reactive
from shiny.express import input, render, ui
import sightings
import mapper

import logging
import app_logging

logger = app_logging.get_logger(__name__)
logger.setLevel(logging.DEBUG)

ui.page_opts(title="Bird Sightings", fillable=True)


@render.text
def get_summary_message() -> str:
    return sightings.SUMMARY_MESSAGE


def build_species_choice_list(species: list) -> dict:
    choice_list = {}
    for item in species:
        choice_list[item] = item
    return choice_list


species_choices = build_species_choice_list(sightings.SPECIES_LIST)

ui.input_select(
    "selected_species", "Choose one species for map", choices=list(species_choices.keys())
)

ui.include_css(Path(__file__).parent / "styles.css")


@render.ui
def map():
    logger.debug("render")
    return htmltools.Tag(species_map()._repr_html_())


@reactive.calc
def species_map():
    selected_species = species_choices[input.selected_species()]
    logger.debug(f"{selected_species=}")
    return mapper.build_map(selected_species)
