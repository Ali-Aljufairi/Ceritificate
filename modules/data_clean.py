import pandas as pd


def Oraginze_data(file_name: str):
    df = pd.read_csv(file_name)
    df["Team"] = df["Team"].apply(lambda x: '"' + x + '"')
    # combine the name and team in a tuple
    df["Name_Team"] = list(zip(df["Name"], df["Team"]))
    return df["Name_Team"].tolist()

def Get_Name(file_name: str):
     df = pd.read_csv(file_name)
     df["Name"].tolist()
     for name in df["Name"].tolist():
        print(name)
    
    