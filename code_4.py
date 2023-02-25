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
    country_code = country_code.upper()
    df = pd.read_csv(big_mac_file)
    querry = f"(iso_a3 == '{country_code}')"
    pbc_df = df.query(querry)
    mean_idk = sum(pbc_df) / len(pbc_df)
    return mean_idk

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    querry = f"(date >='{year}-01-01' and date <= '{year}-12-31')"
    cpby_df = df.query(querry)
    min_idk = cpby_df['dollar_price'].idxmin()
    ycomb_QR = (cpby_df.loc[min_idk]['dollar_price'])
    return round(ycomb_QR,2)

def get_the_most_expensive_big_mac_price_by_year(year):
       df = pd.read_csv(big_mac_file)
       querry = f"(date >='{year}-01-01' and date <= '{year}-12-31')"
       xpby_df = df.query(querry)
       max_idk = xpby_df['dollar_price'].idxmax()
       zcomb_QR = (xpby_df.loc[max_idk]['dollar_price'])
       return round(zcomb_QR,2)

if __name__ == "__main__":
    Q1 = get_big_mac_price_by_year(2006,"mex")
    print(Q1)
    Q2 = get_big_mac_price_by_country("mex")
    print(Q2)
    Q3 = get_the_cheapest_big_mac_price_by_year("2008")
    print(Q3)
    Q4 = get_the_most_expensive_big_mac_price_by_year("2014")
    print(Q4)