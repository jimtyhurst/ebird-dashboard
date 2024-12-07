import mapper


def test_build_title_singular():
    expected_n_sightings = 1
    expected_species_name = "Black Vulture"
    expected_start_date = "2018-09-23"
    expected_end_date = "2018-09-23"
    title = mapper.build_title_string(
        n_sightings=expected_n_sightings,
        species_name=expected_species_name,
        start_date=expected_start_date,
        end_date=expected_end_date,
    )
    assert title.index(str(expected_n_sightings)) == 0
    assert expected_species_name in title
    assert expected_start_date in title


def test_build_title_plural():
    expected_n_sightings = 23
    expected_species_name = "Seagull"
    expected_start_date = "2018-09-23"
    expected_end_date = "2022-11-09"
    title = mapper.build_title_string(
        n_sightings=expected_n_sightings,
        species_name=expected_species_name,
        start_date=expected_start_date,
        end_date=expected_end_date,
    )
    assert title.index(str(expected_n_sightings)) == 0
    assert expected_species_name in title
    assert expected_start_date in title
    assert expected_end_date in title
