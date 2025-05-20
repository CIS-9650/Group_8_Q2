# Riya's code for scraping the top US colleges.

  # From this list of the top 100, we should only return the names and cities for the
  # first 30 of these to the table that we will then use for the API calls. This will
  # reduce the chances of running out of API calls to make based on rate limits
  # form the server.

  # This whole script can be reimagined as a function in the final code that
  # include this + the API call rountine + the sending of data to csv and database.

import requests
from bs4 import BeautifulSoup
import pandas as pd

url_list = {
     'uni':['https://www.topuniversities.com/where-to-study/north-america/united-states/ranked-top-100-us-universities#page-1']
}
def get_university_data(url_list):
    universities = []
    countries = []

    for url in url_list:
        page = requests.get(url)

        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            name_tags = soup.find_all('div', class_='uni_name')
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
