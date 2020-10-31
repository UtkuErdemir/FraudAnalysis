import pandas as pd

csv = None


def get_csv():
    global csv
    if csv is None:
        csv = pd.read_csv('../Datasets/CreditCardDataset/creditcard.csv')
    return csv
