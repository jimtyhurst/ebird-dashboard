import folium
import sightings


# Creates a map centered around the mean latitude and longitude of the sightings.
# TODO:
#   * Calculate bounding box from min/max Latitudes, Longitudes, so all sightings are in view.
#   * Use the bounding box for initial view, rather than arbitrary 'zoom_start'.
def build_map(selected_species: str) -> folium.Map:
    species_sightings = sightings.extract_species_sightings(selected_species)
    sighting_map = folium.Map(
        location=[species_sightings["Latitude"].mean(), species_sightings["Longitude"].mean()],
        zoom_start=3,
    )
    # Adds markers for each sighting location.
    for row in species_sightings.iter_rows():
        folium.Marker(
            # 'row' is a tuple, so you access elements with an integer index.
            location=[row[1], row[2]],  # Latitude, Longitude
            popup=f"{row[3]}: {row[4]} {row[5]}",  # "Location: Date Time"
        ).add_to(sighting_map)

    # Adds title
    start_date = species_sightings["Date"].min()
    end_date = species_sightings["Date"].max()
    title_string = f"Sightings of {selected_species} from {start_date} to {end_date}"
    title_html = f'<h3 align="center"><b>{title_string}</b></h3>'
    sighting_map.get_root().html.add_child(folium.Element(title_html))

    return sighting_map
