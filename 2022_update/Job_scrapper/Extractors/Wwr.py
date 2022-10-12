from requests import get
from bs4 import BeautifulSoup

# extract_jobs
def extract_wwr_jobs(keyword):
    # URL
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    response = get(f"{base_url}{keyword}")

    if response.status_code != 200:
        print("Can't request website. something wrong!")
    else:
        results = []
        # source
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('section', class_="jobs")
        # extracting_jobs
        for job_section in jobs:
            job_posts = job_section.find_all('li')
            job_posts.pop(-1)
            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                company = anchor.find('span', class_="company")
                location = anchor.find('span', class_="region")
                title = anchor.find('span', class_='title')
                job_data = {
                    'link' : f"https://weworkremotely.com{link}", 
                    'company' : company.string,
                    'location' : location.string,
                    'position' : title.string
                }
                results.append(job_data)
        return results