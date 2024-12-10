import polars as pl
from pathlib import Path

DATA_FILE_PATH = Path("data") / "raw" / "MyEBirdData.csv"


def load_data() -> pl.DataFrame:
    return (
        pl.read_csv(
            DATA_FILE_PATH,
            null_values=["X"],
            truncate_ragged_lines=True,
        )
        .filter(pl.col("Count").is_not_null())
        .filter(pl.col("Count").gt(0))
        .sort(
            by=["Date", "Time", "Count", "Common Name"],
            descending=[True, True, True, False],
        )
    )


SIGHTINGS = load_data()


def extract_species_sightings(
    species_common_name: str, df: pl.DataFrame = SIGHTINGS
) -> pl.DataFrame:
    return df.filter(pl.col("Common Name") == species_common_name).select(
        ["Common Name", "Latitude", "Longitude", "Location", "Date", "Time"]
    )


def get_species_list():
    return SIGHTINGS["Common Name"].unique().sort().to_list()


SPECIES_LIST = get_species_list()

SUMMARY_MESSAGE = f"{len(SPECIES_LIST)} species sighted from {SIGHTINGS['Date'].min()} to {SIGHTINGS['Date'].max()}"
