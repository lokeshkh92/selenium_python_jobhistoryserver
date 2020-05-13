from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# resource manager ipaddres and port
ipaddress = "10.0.10.36"
hsport = "19888"
jobname = "MergeAction"

# launch chrome browser and open history server UI
browser = webdriver.Chrome()
browser.get('http://{}:{}/jobhistory'.format(ipaddress, hsport))
table_id = browser.find_element_by_id("jobs_wrapper")
table_tab = 2

# Search for the mergeAction jobs
search_box = browser.find_element_by_xpath('//*[@id="jobs_filter"]/label/input')
search_box.send_keys(jobname)
time.sleep(10)
app_list = []

# Function to get the application id for the merge action
def get_application():
    job_list = []
    row_num=1
    for col in table_id.find_elements(By.CSS_SELECTOR, "td.sorting_1"):
        job_xpath = '//*[@id="jobs"]/tbody/tr[' + str(row_num) + ']/td[4]/a'
        job_id = browser.find_element_by_xpath(job_xpath).get_attribute("text")
        app_id = job_id.replace('job', 'application')
        row_num+=1
        job_list.append(app_id)
    return job_list

#Get the application id over the next page till last page
for i in range(5):
    time.sleep(1)
    tab_path = '//*[@id="jobs_next"]'
    next_table_tab = browser.find_element(By.XPATH, tab_path)
    print("Next_table_tab: {}".format(next_table_tab))
    # if next_table_tab == 'None':
    #     break
    # click on tab
    browser.execute_script("arguments[0].click();", next_table_tab)
    table_tab += 1
    jobs_list = get_application()
    app_list.append(jobs_list)

print app_list
