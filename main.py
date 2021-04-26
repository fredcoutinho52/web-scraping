import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://programathor.com.br/jobs-python'

# getting url content and parsing with beautifulsoup
content = requests.get(url).text
soup = BeautifulSoup(content, 'html.parser')

# finding jobs and their descriptions
jobs = soup.find_all('h3', {'class': 'text-24'})
jobs_description = soup.find_all('div', {'class': 'cell-list-content-icon'})

# getting relevant information from jobs
jobs = [job.text for job in jobs]
jobs_place = [job.find_all('span')[0].text for job in jobs_description]
jobs_location = [job.find_all('span')[1].text for job in jobs_description]

# mounting dataframe to better visualization
jobs_df = {'job': jobs, 'place': jobs_place, 'location': jobs_location}
jobs_df = pd.DataFrame(data=jobs_df)

print(jobs_df)