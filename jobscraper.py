# Finished 180522 0100

from bs4 import BeautifulSoup
import requests


#intro
print('''
Hello, thanks for using jobscraper!

This program takes the front page results from job searching websites such as:
- sg.indeed.com
- jobstreet.com.sg
- sg.jobsdb.com
- sg.linkedin.com
- jobscentral.com.sg

so that you don't have to navigate through different websites for the results.

Some webpages are dynamic javascript built which will complicate things as the program only captures the html document
on load. Javascript elements which are loaded in after that will not be registered. This may cause problems such as 
'Company name unavailable' or 'Link unavailable'. However, restarting the program may work sometimes but the more 
reliable option would be to simply search for the job title in the job portal. Other unavailable information might 
be available on the link provided.

''')


user_keyword = input('Search for job: ')

# sg.indeed.com
keyword = user_keyword.replace(' ', '%20')
html_content = requests.get(f'https://sg.indeed.com/jobs?q={keyword}&l=Singapore&fromage=7&radius=10&sort=date&vjk=d37677b798fae49b').text
soup = BeautifulSoup(html_content, 'lxml')

all_job_titles = soup.findAll('div', class_='cardOutline')
all_posted_dates = soup.findAll('span', class_='date')

print('''
------------------------------------------------------------------------------------------------------------------------
''')
print('sg.indeed.com: \n')
for i, j in enumerate(all_job_titles):
    job = j.div.div.div.div.table.tbody.tr.td  # this is a nightmare
    print(f'Job title: {job.div.h2.a.text}')
    try:
        print(f'Salary: {job.contents[2].div.div.text}')
    except AttributeError:
        print('Salary unavailable')
    try:
        print(f'Company: {job.contents[1].span.text}')
    except AttributeError:
        print(f'Company name unavailable')
    print(f'{all_posted_dates[i].text}')
    print(f"Link: https://sg.indeed.com{job.a['href']}")
    print('\n')


# jobstreet.com.sg
keyword = user_keyword.replace(' ', '-')
html_content = requests.get(f'https://www.jobstreet.com.sg/en/job-search/{keyword}-jobs-in-singapore/?createdAt=7d&sort=createdAt').text
soup = BeautifulSoup(html_content, 'lxml')

all_job_titles = soup.findAll('h1', class_='sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1x _18qlyvc3 _18qlyvca')

print('''
------------------------------------------------------------------------------------------------------------------------
''')
print('jobstreet.com.sg: \n')
for i, j in enumerate(all_job_titles):
    print(f'Job title: {j.text}')
    try:
        if j.parent.parent.contents[3].text[0] == 'S'\
                and j.parent.parent.contents[3].text[1] == 'G' and j.parent.parent.contents[3].text[2] == 'D':
            print(f'Salary: {j.parent.parent.contents[3].text}')
        else:
            print('Salary unavailable')
    except IndexError:
        print('Salary unavailable')
    print(f'Company: {j.parent.contents[1].text}')
    print(f'Posted {j.parent.parent.parent.parent.contents[0].contents[1].contents[0].text}')
    print(f"Link: https://jobstreet.com.sg{j.a['href']}")
    print('\n')


# sg.jobsdb.com
keyword = user_keyword.replace(' ', '+')
html_content = requests.get(f'https://sg.jobsdb.com/j?a=7d&l=Singapore&q={keyword}&r=50&sp=facet_distance&st=date').text
soup = BeautifulSoup(html_content, 'lxml')

all_job_titles = soup.findAll('article', class_='job-card')

print('''
------------------------------------------------------------------------------------------------------------------------
''')
print('sg.jobsdb.com:\n')
for i, j in enumerate(all_job_titles):
    print(f'Job title: {j.div.h3.a.text}')
    try:
        if (j.contents[2].div.text != 'Quick apply'):
            print(f'Salary: {j.contents[2].div.text}')
        else:
            print('Salary not available')
    except AttributeError:
        print('Salary not available')
    print(f'Company: {j.contents[1].contents[0].text}')
    print(f'Location: {j.contents[1].contents[2].text}')
    try:
        print(f'Posted {j.contents[4].text}')
    except IndexError:
        print('Date posted unavailable')
    print(f"Link: https://sg.jobsdb.com{j.div.h3.a['href']}")
    print('\n')


# sg.linkedin.com
keyword = user_keyword.replace(' ', '%20')
html_content = requests.get(f'https://sg.linkedin.com/jobs/search?keywords={keyword}&location=Singapore%2C%20\
Singapore&locationId=&geoId=103804675&f_TPR=r604800&f_PP=103804675&distance=50&position=1&pageNum=0').text
soup = BeautifulSoup(html_content, 'lxml')

all_job_titles = soup.findAll('div', class_='base-search-card__info')

print('''
------------------------------------------------------------------------------------------------------------------------
''')
print('sg.linkedin.com:\n')
for i, j in enumerate(all_job_titles):
    print(f'Job title: {j.h3.text.strip()}')
    print(f'Salary: {j.contents[7].contents[3].text.strip()}')
    try:
        print(f'Company: {j.h4.a.text.strip()}')
    except AttributeError:
        print('Company name unavailable')
    print(f'Posted: {j.div.time.text.strip()}')
    try:
        print(f"Link: {j.parent.a['href']}")
    except TypeError:
        print('Link unavailable')
    print('\n')


# jobscentral.com.sg
keyword = user_keyword.replace(' ', '+')
html_content = requests.get(f'https://jobscentral.com.sg/jobs?emp=&keywords={keyword}&location=&sort=date_desc').text
soup = BeautifulSoup(html_content, 'lxml')

all_job_titles = soup.findAll('li', class_='data-results-content-parent relative')

print('''
------------------------------------------------------------------------------------------------------------------------
''')
print('jobscentral.com.sg:\n')
for i, j in enumerate(all_job_titles):
    print(f'Job title: {j.div.contents[3].contents[3].text}')
    print(f'Salary: {j.div.contents[3].contents[9].contents[3].text}')
    print(f'Company: {j.div.contents[3].contents[5].contents[1].text}')
    print(f'Location: {j.div.contents[3].contents[5].contents[3].text}')
    try:
        print(f'Job type: {j.div.contents[3].contents[5].contents[5].text}')
    except IndexError:
        print('Job type unavailable')
    print(f'Posted: {j.div.contents[3].div.text}')
    print(f"Link: https://jobscentral.com.sg{j.a['href']}")
    print('\n')
