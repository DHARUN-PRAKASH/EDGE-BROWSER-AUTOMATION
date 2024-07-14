from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# List of search queries
search_queries = [
    "Python",
    "JavaScript",
    "Node.js",
    "MongoDB vs SQL",
    "SQL",
    "MongoDB",
    "React vs Angular",
    "React",
    "Angular",
    "Machine learning",
    "Neural networks",
    "Hypothesis testing in statistics",
    "Web development trends 2024",
    "Face recognition technology",
    "Home security systems",
    "Git version control",
    "Express.js tutorial",
    "Data models in MongoDB",
    "C programming language",
    "Django vs Flask",
    "REST API",
    "GraphQL",
    "Docker",
    "Kubernetes",
    "CI/CD pipelines",
    "Agile methodology",
    "Scrum vs Kanban",
    "DevOps practices",
    "Microservices architecture",
    "Serverless computing"
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
    
    # Close previous tabs
    for handle in driver.window_handles[:-1]:
        driver.switch_to.window(handle)
        driver.close()
    
    # Switch back to the new tab
    driver.switch_to.window(driver.window_handles[-1])
