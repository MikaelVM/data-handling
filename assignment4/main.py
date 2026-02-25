"""Solutions to assignment 4 - Theme Introduction to Pandas."""
import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt


if __name__ == "__main__":
    path_to_data = Path("data/DKHousingPricesSample100k.csv")

    dataframe = pd.read_csv(path_to_data,
                            delimiter=',',
                            dtype={"date": "string",
                                   "quarter": "string",
                                   "house_id": "int",
                                   "house_type": "string",
                                   "sales_type": "string",
                                   "year_build": "int",
                                   "purchase_price": "int",
                                   "%_change_between_offer_and_purchase": "float",
                                   "no_rooms": "int",
                                   "sqm": "int",
                                   "sqm_price": "float",
                                   "address": "string",
                                   "zip_code": "int",
                                   "city": "string",
                                   "area": "string",
                                   "region": "string",
                                   "nom_interest_rate%": "float",
                                   "dk_ann_infl_rate%": "float",
                                   "yield_on_mortgage_credit_bonds%": "float"}
                            )
    pd.to_datetime(dataframe["date"], format="%Y-%m-%d")

    print(dataframe.head(10))

    print(dataframe.groupby("region")["purchase_price"].mean())

    print(dataframe.groupby("house_type")["purchase_price"].mean())

    dataframe.groupby("region")["purchase_price"].mean().plot(kind="bar", title="Average purchase price by house type")
    plt.show()

    dataframe.groupby("house_type")["purchase_price"].mean().plot(kind="bar", title="Average purchase price by house type")
    plt.show()

