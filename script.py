from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
driver = webdriver.Chrome("C:\\Users\\Suvid Singhal\\Desktop\\chromedriver")

url = 'https://hk.jobsdb.com/hk/jobs/information-technology/1'


driver.get(url)
timeout = 5
jobTitles_element = driver.find_elements_by_xpath("//a[@*]//div[@*]")
jobTitles = [x.text for x in jobTitles_element]

while("" in jobTitles):
    jobTitles.remove("")

jobTitles = jobTitles[4:-3]
i = iter(jobTitles)
jobTitles = dict(zip(i, i))

for item in jobTitles:
    print("Job : {}\nEmployer : {}\n".format(item,jobTitles[item]))
