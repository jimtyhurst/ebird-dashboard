import sightings


def test_load_data():
    df = sightings.load_data()
    assert df.shape[0] > 10_000
    assert df.shape[1] == 23


def test_extract_species_sightings():
    df = sightings.extract_species_sightings(
        "American Crow",
    )
    assert df.shape[0] > 600
    assert df.shape[1] == 6


def test_get_species_choice_list():
    assert isinstance(sightings.SPECIES_CHOICE_LIST, dict)
    assert sightings.SPECIES_CHOICE_LIST["Acorn Woodpecker"] == "Acorn Woodpecker"
