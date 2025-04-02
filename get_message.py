import pandas as pd

URL = "https://docs.google.com/document/d/e/2PACX-1vSZ1vDD85PCR1d5QC2XwbXClC1Kuh3a4u0y3VbTvTFQI53erafhUkGot24ulET8ZRqFSzYoi3pLTGwM/pub"


def fetch_grid_dataframe(grid_url):
    grid_list = pd.read_html(grid_url)
    grid = grid_list[0]
    grid.columns = ["x", "character", "y"]
    grid = grid.iloc[1:].reset_index(drop=True)
    grid["x"] = grid["x"].astype(int)
    grid["y"] = grid["y"].astype(int)
    grid["character"] = grid["character"].apply(
        lambda character: character.encode("latin1").decode("utf-8")
    )
    return grid


def format_grid(table):
    max_x = table["x"].max()
    max_y = table["y"].max()
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for _, row in table.iterrows():
        grid[row["y"]][row["x"]] = row["character"]
    return "\n".join("".join(row) for row in reversed(grid))


def print_grid(grid_url):
    grid = fetch_grid_dataframe(grid_url)
    print(format_grid(grid))


if __name__ == "__main__":
    print_grid(URL)
