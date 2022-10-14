from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Bot_Fix
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# browser_Auto
browser = webdriver.Chrome(r"C:/Users/chromedriver.exe")

# page_count
def get_page_count(keyword):
    base_url="https://kr.indeed.com/jobs?q="
    browser.get(f"{base_url}{keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", class_="css-jbuxu0")
    if pagination == None:
        return 1
    pages = pagination.find_all("div", class_="css-tvvxwd")
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count

# extract_jobs
def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    results = []
    for page in range(pages):
        base_url = "https://kr.indeed.com/jobs?"
        final_url = f"{base_url}q={keyword}&start={page*10}"
        browser.get(final_url)

        # page_source
        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list=(soup.find("ul", class_="jobsearch-ResultsList"))
        jobs=job_list.find_all("li", recursive=False)

        # extracting_job
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                link = anchor['href']
                title = anchor['aria-label']
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                if "," not in company.string:
                    job_data = {
                        'link': f"https://kr.indeed.com{link}",
                        'company': company.string.replace(","," "),
                        'location': location.string,
                        'position': title.replace(","," ")
                    }
                else:
                    job_data = {
                        'link': f"https://kr.indeed.com{link}",
                        'company': company.string.replace(","," "),
                        'location': location.string.replace(","," "),
                        'position': title.replace(","," ")
                    }
                results.append(job_data)
    return results