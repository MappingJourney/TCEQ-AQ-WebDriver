from selenium.webdriver.support.ui import Select
import csv


class AirQualityScraper:
    def __init__(self, driver):
        self.driver = driver

    def site_select(self, site):
        selected_site = self.driver.find_element_by_name('select_site')
        dropdown_list = Select(selected_site)
        dropdown_list.select_by_value(site)

    def show_parameters(self, ):
        index = 1
        parameters = self.driver.find_elements_by_xpath('//*[@id="meteostar_wrapper"]/form/div[3]/table/tbody/tr')
        for parameter in parameters:
            print(f"{index}. {parameter.text}")
            index = index + 1

    def data_copy(self, parameter, start_year, end_year, file):
        for year in range(start_year, end_year + 1):
            if year == start_year:
                # Selects first year to get Date and hours headers
                year_select = self.driver.find_element_by_name('user_year')
                year_dropdown = Select(year_select)
                year_dropdown.select_by_value(str(year))

                # Chooses Parameter
                self.driver.find_element_by_xpath(
                    '//*[@id="meteostar_wrapper"]/form/div[3]/table/tbody/tr['
                    + str(parameter) + ']/td/input').click()

                # Selects CSV Format
                self.driver.find_element_by_xpath('//*[@id="meteostar_wrapper"]/form/div[5]/input[2]').click()

                # Generates Report
                self.driver.find_element_by_xpath('//*[@id="meteostar_wrapper"]/form/input[4]').click()

                # Collects data
                pre_data = self.driver.find_element_by_xpath('//*[@id="meteostar_wrapper"]/pre')
                string_data = pre_data.text
                relevant_data = string_data[string_data.find('Date,'):].splitlines()
                data_reader = csv.reader(relevant_data)
                data = list(data_reader)
                # Writes data to file
                with open("Data/"+str(file)+".csv", "w", newline='') as datafile:
                    data_writer = csv.writer(datafile)
                    data_writer.writerows(data)
            else:
                # Selects remaining years only by data
                year_select = self.driver.find_element_by_name('user_year')
                year_dropdown = Select(year_select)
                year_dropdown.select_by_value(str(year))

                # Generates new report
                self.driver.find_element_by_xpath(
                    '//*[@id="meteostar_wrapper"]/form[2]/table/tbody/tr[2]/td/input').click()

                # Collects data
                pre_data = self.driver.find_element_by_xpath('//*[@id="meteostar_wrapper"]/pre')
                string_data = pre_data.text
                relevant_data = string_data[string_data.find('01/01'):].splitlines()
                data_reader = csv.reader(relevant_data)
                data = list(data_reader)
                # Writes data to file
                with open("Data/"+str(file)+".csv", "a+", newline='') as datafile:
                    data_writer = csv.writer(datafile)
                    data_writer.writerows(data)

        print(str(file)+" Completed")

        # Goes back
        self.driver.find_element_by_xpath('//*[@id="meteostar_wrapper"]/form[1]/input[6]').click()
