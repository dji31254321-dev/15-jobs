import requests
from bs4 import BeautifulSoup



def search_saramin(keyword, pages):
    jobs = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"}
    for i in range(pages):
        page_num = i + 1
        url = f"https://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword={keyword}&recruitPage={page_num}&recruitSort=relation&recruitPageCount=40&inner_com_type=&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&show_applied=&quick_apply=&except_read=&ai_head_hunting="
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        lis = soup.find_all("div", class_="item_recruit")

        for li in lis:
            company = li.find("div", class_ = "area_corp").find("a").text.strip()
            title_tag = li.find("div", class_ = "area_job").find("h2", class_ = "job_tit").find("a")
            title = title_tag.text.strip()
            location = li.find("div", class_ = "job_condition").find_all("span")[0].text.strip()
            
            link = "https://www.saramin.co.kr" + title_tag.get("href")
            
            job_data = {
                "company": company,
                "title": title,
                "location": location,
                "link": link
            }

            jobs.append(job_data)
            
    return jobs



def search_incruit(keyword, pages):     

    jobs = []
    for i in range(pages):
        page = i * 30
        
        url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno=1{page}"
        print(url)


        response = requests.get(url)


        soup = BeautifulSoup(response.text, "html.parser")


        lis = soup.find_all("li", class_ = "c_col")






        for li in lis:
            
            company = li.find("a", class_ = "cpname").text.strip()
            title = li.find("div", class_ = "cell_mid").find("div", class_ = "cl_top").find("a").text.strip()
            location = li.find("div", class_ = "cl_md").find_all("span")[0].text.strip()
            link = li.find("div", class_ = "cell_mid").find("div", class_ = "cl_top").find("a").get("href")
            
            job_data = {
                "company": company,
                "title": title,
                "location": location,
                "link": link
            }

            jobs.append(job_data)
    return jobs

keyword = "파이썬"
url = f"https://www.jobkorea.co.kr/Search?stext={keyword}&tabType=recruit&Page_No=1"

response = requests.get(url)