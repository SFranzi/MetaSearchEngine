from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

def expertenservice(searchterm):
	results = []
	driver = webdriver.Firefox()
	driver.get('https://www.uni-hamburg.de/newsroom/presse/expertenservice.html') 

	inputElement = driver.find_element_by_id("Test")
	inputElement.send_keys(searchterm)

	time.sleep(2)

	oap_results = driver.find_elements_by_class_name("oap-result")

	result_list = []
	for result in oap_results:
		if result.text: 
			name = result.find_element_by_class_name("oap-result-title").text
			tags = []
			for tag in result.find_elements_by_class_name("tag"): 
				tags.append(tag.text)
			infos = dict()
			for info in result.find_elements_by_class_name("oap-result-info"):
				array = info.text.split("\n")
				infos[array[0]] = array[1]
			result_list.append({"Titel": name, "Schwerpunkte": tags, **infos})
	return result_list
