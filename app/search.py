from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

def expertenservice(searchterm):
	results = []
	driver = webdriver.Firefox()
	driver.get('https://www.uni-hamburg.de/newsroom/presse/expertenservice.html') 

	inputElement = driver.find_element_by_id("Test")
	inputElement.send_keys(searchterm)
	#submitButton = driver.find_element_by_type("submit")
	#submitButton.click()

	time.sleep(2)
	#result = driver.find_element_by_class_name("oap-results")
	oap_results = driver.find_elements_by_class_name("oap-result")

	#result_list = []
	#for result in oap_results: 
		#f result.text:
			#contact = dict()
			#text = result.text
			#array = text.split("\n")
			#for element in array: 
				#contact['name'] = element
			#result_list.append(contact)
	#return result_list

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
			result_list.append({"name": name, "tags": tags, **infos})
	return result_list


	#print(schwerpunkte)
	#print(result.text)
	#driver.quit()

	#for i in range(len(array)): 
				#print(array[i])
			#if array[1] == 'Schwerpunkte'
				#schwerpunkte = array[1]
			#else 
		
