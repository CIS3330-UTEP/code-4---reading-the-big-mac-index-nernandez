import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    country_code = country_code.upper()
    df = pd.read_csv(big_mac_file)
    querry = f"(iso_a3 == '{country_code}' and date >='{year}-01-01' and date <= '{year}-12-31')"
    pby_df = df.query(querry)
    min_idk = pby_df['dollar_price'].idxmin()
    comb_QR = (pby_df.loc[min_idk]['dollar_price'])
    return round(comb_QR,2)

def get_big_mac_price_by_country(country_code):
    pass # Remove this line and code your function

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    Q1 = get_big_mac_price_by_year(2006,"mex")
    print(Q1)