import pandas as pd


def load_data(uploaded_file):

    df = pd.read_excel(
        uploaded_file,
        sheet_name="Sales_Data"
    )

    df["Date"] = pd.to_datetime(
        df["Date"]
    )

    return df