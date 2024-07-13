from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# List of search queries
search_queries = [
    "Python programming",
    "JavaScript tutorials",
    "Node.js best practices",
    "MongoDB vs SQL",
    "React vs Angular",
    "Machine learning basics",
    "Neural networks explained",
    "Hypothesis testing in statistics",
    "Web development trends 2024",
    "Face recognition technology",
    "Home security systems",
    "Git version control",
    "Express.js tutorial",
    "Data models in MongoDB",
    "C programming language",
]


options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument(r'E:\PROJECT\BROWSER-AUTOMATION\edgedriver_win32\msedgedriver.exe')
options.add_argument('profile-directory=Profile 1')  

service = Service(r'E:\PROJECT\BROWSER-AUTOMATION\edgedriver_win32\msedgedriver.exe')
driver = webdriver.Edge(service=service, options=options)
time.sleep(5)


driver.get("https://www.bing.com")
time.sleep(2) 
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(search_queries[0])
search_box.send_keys(Keys.RETURN)
time.sleep(5) 


for query in search_queries[1:]:
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get("https://www.bing.com")
    time.sleep(2) 
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)  


