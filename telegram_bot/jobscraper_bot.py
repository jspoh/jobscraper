# Finished 180522 0100

from bs4 import BeautifulSoup
import requests
import time


def search_all(user_keyword, update):
    print(f'Searching all {user_keyword}..')
    with open('results/alljobs_jobscraper.txt', mode='w', encoding='utf-8') as f:

        # sg.indeed.com
        keyword = user_keyword.replace(' ', '%20')
        html_content = requests.get(f'https://sg.indeed.com/jobs?q={keyword}&l=Singapore&fromage=7&radius=10&sort=date&vjk=d37677b798fae49b').text
        soup = BeautifulSoup(html_content, 'lxml')

        all_job_titles = soup.findAll('div', class_='cardOutline')
        all_posted_dates = soup.findAll('span', class_='date')

        f.write('''
        ------------------------------------------------------------------------------------------------------------------------
        ''')
        f.write('sg.indeed.com: \n\n\n')
        for i, j in enumerate(all_job_titles):
            job = j.div.div.div.div.table.tbody.tr.td  # this is a nightmare
            f.write(f'Job title: {job.div.h2.a.text}\n')
            try:
                f.write(f'Salary: {job.contents[2].div.div.text}\n')
            except AttributeError:
                f.write('Salary unavailable\n')
            try:
                f.write(f'Company: {job.contents[1].span.text}\n')
            except AttributeError:
                f.write(f'Company name unavailable\n')
            f.write(f'{all_posted_dates[i].text}\n')
            f.write(f"Link: https://sg.indeed.com{job.a['href']}\n")
            f.write('\n\n')

        # jobstreet.com.sg
        keyword = user_keyword.replace(' ', '-')
        html_content = requests.get(f'https://www.jobstreet.com.sg/en/job-search/{keyword}-jobs-in-singapore/?createdAt=7d&sort=createdAt').text
        soup = BeautifulSoup(html_content, 'lxml')

        all_job_titles = soup.findAll('h1', class_='sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1x _18qlyvc3 _18qlyvca')

        f.write('''
        ------------------------------------------------------------------------------------------------------------------------
        ''')
        f.write('jobstreet.com.sg: \n\n\n')
        for i, j in enumerate(all_job_titles):
            f.write(f'Job title: {j.text}\n')
            try:
                if j.parent.parent.contents[3].text[0] == 'S' \
                        and j.parent.parent.contents[3].text[1] == 'G' and j.parent.parent.contents[3].text[2] == 'D':
                    f.write(f'Salary: {j.parent.parent.contents[3].text}\n')
                else:
                    f.write('Salary unavailable\n')
            except IndexError:
                f.write('Salary unavailable\n')
            f.write(f'Company: {j.parent.contents[1].text}\n')
            f.write(f'Posted {j.parent.parent.parent.parent.contents[0].contents[1].contents[0].text}\n')
            f.write(f"Link: https://jobstreet.com.sg{j.a['href']}\n")
            f.write('\n\n')

        # sg.jobsdb.com
        keyword = user_keyword.replace(' ', '+')
        html_content = requests.get(f'https://sg.jobsdb.com/j?a=7d&l=Singapore&q={keyword}&r=50&sp=facet_distance&st=date').text
        soup = BeautifulSoup(html_content, 'lxml')

        all_job_titles = soup.findAll('article', class_='job-card')

        f.write('''
        ------------------------------------------------------------------------------------------------------------------------
        ''')
        f.write('sg.jobsdb.com:\n\n\n')
        for i, j in enumerate(all_job_titles):
            f.write(f'Job title: {j.div.h3.a.text}\n')
            try:
                if (j.contents[2].div.text != 'Quick apply'):
                    f.write(f'Salary: {j.contents[2].div.text}\n')
                else:
                    f.write('Salary not available\n')
            except AttributeError:
                f.write('Salary not available\n')
            f.write(f'Company: {j.contents[1].contents[0].text}\n')
            f.write(f'Location: {j.contents[1].contents[2].text}\n')
            try:
                f.write(f'Posted {j.contents[4].text}\n')
            except IndexError:
                f.write('Date posted unavailable\n')
            f.write(f"Link: https://sg.jobsdb.com{j.div.h3.a['href']}\n")
            f.write('\n\n')

        # sg.linkedin.com
        keyword = user_keyword.replace(' ', '%20')
        html_content = requests.get(f'https://sg.linkedin.com/jobs/search?keywords={keyword}&location=Singapore%2C%20\
Singapore&locationId=&geoId=103804675&f_TPR=r604800&f_PP=103804675&distance=50&position=1&pageNum=0').text
        soup = BeautifulSoup(html_content, 'lxml')

        all_job_titles = soup.findAll('div', class_='base-search-card__info')

        f.write('''
        ------------------------------------------------------------------------------------------------------------------------
        ''')
        f.write('sg.linkedin.com:\n\n\n')
        for i, j in enumerate(all_job_titles):
            f.write(f'Job title: {j.h3.text.strip()}\n')
            f.write(f'Salary: {j.contents[7].contents[3].text.strip()}\n')
            try:
                f.write(f'Company: {j.h4.a.text.strip()}\n')
            except AttributeError:
                f.write('Company name unavailable\n')
            f.write(f'Posted: {j.div.time.text.strip()}\n')
            try:
                f.write(f"Link: {j.parent.a['href']}\n")
            except TypeError:
                f.write('Link unavailable\n')
            f.write('\n\n')

        # jobscentral.com.sg
        keyword = user_keyword.replace(' ', '+')
        html_content = requests.get(f'https://jobscentral.com.sg/jobs?emp=&keywords={keyword}&location=&sort=date_desc').text
        soup = BeautifulSoup(html_content, 'lxml')

        all_job_titles = soup.findAll('li', class_='data-results-content-parent relative')

        f.write('''
        ------------------------------------------------------------------------------------------------------------------------
        ''')
        f.write('jobscentral.com.sg:\n\n\n')
        for i, j in enumerate(all_job_titles):
            f.write(f'Job title: {j.div.contents[3].contents[3].text}\n')
            f.write(f'Salary: {j.div.contents[3].contents[9].contents[3].text}\n')
            f.write(f'Company: {j.div.contents[3].contents[5].contents[1].text}\n')
            f.write(f'Location: {j.div.contents[3].contents[5].contents[3].text}\n')
            try:
                f.write(f'Job type: {j.div.contents[3].contents[5].contents[5].text}\n')
            except IndexError:
                f.write('Job type unavailable\n')
            f.write(f'Posted: {j.div.contents[3].div.text}')
            f.write(f"Link: https://jobscentral.com.sg{j.a['href']}\n")
            f.write('\n\n')

        f.write('end')

    print('''Done!''')

