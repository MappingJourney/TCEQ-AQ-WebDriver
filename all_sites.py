from selenium import webdriver

# Opening and creating file
site_list = open("site_list.txt", 'w')

# Driver and the URL
driver = webdriver.Chrome()
driver.get("https://www.tceq.texas.gov/cgi-bin/compliance/monops/yearly_summary.pl")

# Selects the air quality site
site_element = driver.find_element_by_name('select_site')
site_options = site_element.find_elements_by_tag_name('option')
for option in site_options:
    site_list.write(option.get_attribute('value')+'\n')
