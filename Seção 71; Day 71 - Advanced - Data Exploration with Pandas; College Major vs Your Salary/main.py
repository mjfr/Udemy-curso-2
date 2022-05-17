import time

import pandas as pd
from bs4 import BeautifulSoup
import requests


def made_in_google_colab():
    df = pd.read_csv('salaries_by_college_major.csv')

    print(df.head())

    print(df.shape)

    print(df.columns)

    print(df.isna())

    print(df.tail())

    clean_df = df.dropna()

    print(clean_df.tail())

    print(clean_df['Starting Median Salary'])

    print(clean_df['Starting Median Salary'].max())

    print(clean_df['Starting Median Salary'].idxmax())

    print(clean_df['Undergraduate Major'].loc[43])

    print(clean_df['Undergraduate Major'][43])

    print(clean_df.loc[43])

    # Challenge
    # What college major has the highest mid-career salary? How much do graduates
    # with this major earn? (Mid-career is defined as having 10+ years
    # of experience).
    print(clean_df['Mid-Career Median Salary'].max())

    print(clean_df['Mid-Career Median Salary'].idxmax())

    print(clean_df['Undergraduate Major'][8])

    # Which college major has the lowest starting salary and how much do graduates
    # earn after university?
    print(clean_df['Starting Median Salary'].min())

    print(clean_df['Starting Median Salary'].idxmin())

    print(clean_df['Undergraduate Major'][49])

    # Which college major has the lowst mid-career salary and how much can people
    # expect to earn with this degree?
    print(clean_df['Mid-Career Median Salary'].min())

    print(clean_df['Mid-Career Median Salary'].idxmin())

    print(clean_df['Undergraduate Major'][18])

    print(clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary']))

    spread_col = clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])

    print(clean_df.insert(1, 'Spread', spread_col))

    print(clean_df.head())

    low_risk = clean_df.sort_values('Spread')

    print(low_risk[['Undergraduate Major', 'Spread']].head())

    highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary',
                                             ascending=False)

    print(highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())

    high_risk = clean_df.sort_values('Spread', ascending=False)

    print(high_risk[['Undergraduate Major', 'Spread']].head())

    print(clean_df.groupby('Group').count())

    print(clean_df.groupby('Group').mean())

    pd.options.display.float_format = '{:,.2f}'.format

    print(clean_df.groupby('Group').mean())


PAYSCALE_URL = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/"


def scraping_newer_data():
    response_pages = requests.get(f"{PAYSCALE_URL}1")  # The starting page, will only get our page_number and title_list
    web_page_pages = response_pages.text
    soup_pages = BeautifulSoup(markup=web_page_pages, parser="lxml.parser", features="lxml")
    page_number = [page.getText() for page in soup_pages.find_all(name="div", class_="pagination__btn--inner")]
    title_list = [title.getText().replace("Rank", "").replace("% High Meaning", "") for title in
                  soup_pages.find_all(name="th", class_="data-table__header")]

    major_list = []
    for page in range(1, int(page_number[-2])+1):
        response = requests.get(f"{PAYSCALE_URL}{page}")  # Will loop through the currently 34 pages getting the lists
        web_page = response.text
        soup = BeautifulSoup(markup=web_page, parser="lxml.parser", features="lxml")
        major_list.append([major.getText().replace(",", "").replace("$", "").replace("%", "") for major in
                           soup.find_all(name="span", class_="data-table__value")])  # Each page will give a 25 length
        # result list

    with open(file="salaries_by_college_major_updated.csv", mode="w") as data:
        aux = 0  # An aux variable that helps to put the commas in the right place
        for title in title_list:
            aux += 1
            if aux != 1 and aux != 6:
                data.write(f"{title},")
        data.write("\n")
        aux = 0  # An aux variable that will count to six so every 6 additions a linebreak will happen.
        for page in range(0, int(page_number[-2])):  # An external loop to act as a page counter
            for major in major_list[page]:  # The major list is a list of lists. Each internal list is composed of a max
                # of 25 results. So currently we have 33 pages + 2 results, that is, 827 entries.
                if aux == 6:
                    aux = 0
                    data.write("\n")
                aux += 1
                if aux != 1 and aux != 6:
                    data.write(f"{major},")


if __name__ == '__main__':
    # made_in_google_colab()
    scraping_newer_data()
