from bs4 import BeautifulSoup
from time import sleep
import requests


def find_jobs():
    html_text = requests.get('https://realpython.github.io/fake-jobs').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_='card')

    print(jobs)
    for job in jobs:
        job_title = job.find('h2', class_='title').text.strip()
        job_company = job.find('h3', class_='company').text.strip()
        job_location = job.find('p', class_='location').text.strip()
        print(job_title)
        with open('posts/jobs.txt', 'a') as f:
            f.write(f"Job Title : {job_title}, Job Company : {job_company}, Job Location : {job_location} \n")


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes ...')
        sleep(time_wait * 10)
