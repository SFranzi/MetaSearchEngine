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

	for r in oap_results: 
		if r.text:
			#title = driver.find_element_by_class_name("oap-result-title")
			#print(title.text)
			#print(r.text) 
			#print("--------------------------------------------------")

			text = r.text
			array = text.split("\n")
			#print(array)


			title = array[0]

			#for i in range(len(array)): 
				#print(array[i])
			#if array[1] == 'Schwerpunkte'
				#schwerpunkte = array[1]
			#else 
			print(title)
			results.append(title)

	return results

	#print(schwerpunkte)
	#print(result.text)
	#driver.quit()
		
