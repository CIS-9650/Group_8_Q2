# uni_climate_data.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

url_list = {
     'uni':['https://www.topuniversities.com/world-university-rankings/2024']
}

def get_university_data(url_list):
    universities = []
    countries = []

    for url in url_list:
        page = requests.get(url)

        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')

            # NOTE: Actual site uses JavaScript. You must inspect and adjust these selectors.
            name_tags = soup.find_all('a', class_='uni-link')
            country_tags = soup.find_all('div', class_='location')

            for name_tag, country_tag in zip(name_tags, country_tags):
                university = name_tag.get_text(strip=True)
                country = country_tag.get_text(strip=True)
                universities.append(university)
                countries.append(country)

    # Create the DataFrame
    data = {
        'University': universities,
        'Country': countries
    }

    df = pd.DataFrame(data)
    return df
uni_df = get_university_data(url_list['uni'])
uni_df
# final code for creating a table with 
# universities and data on their climate
