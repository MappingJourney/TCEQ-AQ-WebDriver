from tceq_class import AirQualityScraper
from selenium import webdriver


url = 'https://www.tceq.texas.gov/cgi-bin/compliance/monops/yearly_summary.pl'
site = input("Enter the site you want data for as it appears in site_list.txt: ")
print("**************************************************************")

driver = webdriver.Chrome()
driver.get(url)

tceq = AirQualityScraper(driver)

tceq.site_select(site)
tceq.show_parameters()

print("**************************************************************")
parameters = input("Enter the parameter numbers you want data for (e.g. 5,6,1,): ")
start_year = int(input("Enter the first year of your data (e.g. 2016): "))
end_year = int(input("Enter the end year of your data (e.g. 2020): "))
files = input("Enter the names of your data files (e.g. ID_Parameter_Years(2000-2020), ID_Parameter_Years(2010-2015): ")
print("**************************************************************")
print("Gathering Data")

parameter_list = parameters.split(sep=',')
file_list = files.split(sep=', ')

iteration = 0

for parameter in parameter_list:
    tceq.data_copy(parameter, start_year, end_year, file_list[iteration])
    iteration = iteration + 1

driver.close()
print("**************************************************************")
print("End of program.\nYour data is now in the Data folder.")
