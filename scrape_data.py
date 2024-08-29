import requests
from bs4 import BeautifulSoup
import json

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7",
    "Cache-Control": "no-cache",
    "Cookie": "id=36a94ced-a94d-4909-868c-a1cbbe1340e4; amp_e56929=cHf7BvP59o-oScopA2_p3g...1hv9hur97.1hv9ih73n.0.0.0; amp_e56929_goclasses.in=cHf7BvP59o-oScopA2_p3g...1hv9hurak.1hv9ih78n.5c.3q.96; c_login_token=1700545610100; datadome=MkhLHFZbLAzNVhbUH4YQ15OWms768cK1gV3pKdgRgfPl5N8s4SljZjBCMK6Nu6mlVtBaxoyuLQjkDGVoy0pLfqrIvd9YnhghV8ngZ_IpEEqsQvXXnZpROqxN8gl~YJ3L; SESSIONID=6AA6C95BF0728C466EE1870B0BD6CE32; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=en",
    "Pragma": "no-cache",
    "Priority": "u=0, i",
    "Sec-Ch-Device-Memory": "8",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "Sec-Ch-Ua-Arch": "\"x86\"",
    "Sec-Ch-Ua-Full-Version-List": "\"Google Chrome\";v=\"125.0.6422.142\", \"Chromium\";v=\"125.0.6422.142\", \"Not.A/Brand\";v=\"24.0.0.0\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Model": "\"\"",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

def scrape_quizzes(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    data = []
    rows = soup.find_all('tr', class_='t-row')
    
    for row in rows:
        cols = row.find_all('td', class_='t-info')
        if len(cols) >= 6:
            a_tag = cols[1].find('a')
            link = a_tag['href'] if a_tag else None
            quiz_data = {
                'Exam Name': cols[0].text.strip(),
                'Test Link': link,
                'Exam Date': cols[2].text.strip(),
                'Course': cols[3].text.strip(),
                'Topics': cols[4].text.strip(),
                'Availability': cols[5].text.strip()
            }
            data.append(quiz_data)
    
    return data

def scrape_test_series(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    data = []
    rows = soup.find_all('tr', class_='t-row')
    
    for row in rows:
        cols = row.find_all('td', class_='t-info')
        if len(cols) >= 4:
            a_tag = cols[1].find('a')
            link = a_tag['href'] if a_tag else None
            test_data = {
                'Exam Name': cols[0].text.strip(),
                'Test Link': link,
                'Exam Date': cols[2].text.strip(),
                'Topics': cols[3].text.strip()
            }
            data.append(test_data)
    
    return data

quizzes_url = "https://www.goclasses.in/s/pages/gate-cse-weekly-quizzes"
test_series_url = "https://www.goclasses.in/s/pages/gate-cse-test-series"

quizzes_data = scrape_quizzes(quizzes_url)
test_series_data = scrape_test_series(test_series_url)

# Convert data to JSON and print
print(json.dumps(quizzes_data, indent=2))
print(json.dumps(test_series_data, indent=2))