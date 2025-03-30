import pandas as pd

def extract_table(url):
    table_list = pd.read_html(url)
    table = table_list[0]
    table.columns = ["x", "character", "y"]
    table = table.iloc[1:].reset_index(drop=True)
    table["x"] = table["x"].astype(int)
    table["y"] = table["y"].astype(int)
    table["character"] = table["character"].apply(lambda c: c.encode("latin1").decode("utf-8"))
    return table

def grid_map(table):
    max_x = table["x"].max()
    max_y = table["y"].max()
    grid = [[" " for i in range(max_x + 1)] for i in range(max_y + 1)]
    for i, row in table.iterrows():
        grid[row["y"]][row["x"]] = row["character"]
    return "\n".join("".join(row) for row in reversed(grid))

def print_grid(url):
    table = extract_table(url)
    print(grid_map(table))

url = "https://docs.google.com/document/d/e/2PACX-1vSZ1vDD85PCR1d5QC2XwbXClC1Kuh3a4u0y3VbTvTFQI53erafhUkGot24ulET8ZRqFSzYoi3pLTGwM/pub"
print_grid(url)
