import pandas as pd
import time
from selenium import webdriver

## Load vessel ids
imo_nos_df = pd.read_excel("Vessel_Identifier.xlsx")
imo_nos = imo_nos_df['IMO No.'].tolist()
# imo_nos = imo_nos[0:10]

## Launch Chrome driver
chrome_path = "/Users/shenghao/Desktop/data-repos/ey-web-scraping-assessment/chromedriver"
driver = webdriver.Chrome(chrome_path)
vessels = []

print("Start scraping vessel data...")
start_time = time.time()

for imo_no in imo_nos:
	vessel_info = {
		'IMO No.': str(imo_no),
		'AIS Type': '',
		'Flag': '',
		'Destination': '',
		'ETA': '',
		'MMSI': '',
		'Callsign': '',
		'Length': '',
		'Beam': '',
		'Current draught': '',
		'Course': '',
		'Speed': '',
		'Coordinates': '',
		'Last report': ''
	}

	search_result_url = "https://www.vesselfinder.com/vessels?name=" + str(imo_no)
	driver.get(search_result_url)
	vessel_url_container = driver.find_elements_by_class_name('ship-link')
	if len(vessel_url_container) > 0:
		vessel_url = vessel_url_container[0].get_attribute("href")
		print(vessel_url)

		driver.get(vessel_url)
		vessel_params_table = driver.find_element_by_class_name('tparams')
		vessel_rows = vessel_params_table.find_elements_by_tag_name('tr')

		
		for row in vessel_rows:
			param_cells = row.find_elements_by_tag_name('td')
			if len(param_cells) == 2:
				if param_cells[0].text == 'AIS Type':
					vessel_info['AIS Type'] = param_cells[1].text.strip()
				elif param_cells[0].text == 'Flag':
					vessel_info['Flag'] = param_cells[1].text.strip()
				elif param_cells[0].text == 'Destination':
					vessel_info['Destination'] = param_cells[1].text.strip()
				elif param_cells[0].text == 'ETA':
					vessel_info['ETA'] = param_cells[1].text.strip()
				elif param_cells[0].text == 'IMO / MMSI' and param_cells[1].text != '-':
					vessel_info['MMSI'] = param_cells[1].text.split('/')[1].strip()
				elif param_cells[0].text == 'Callsign':
					vessel_info['Callsign'] = param_cells[1].text.strip()
				elif param_cells[0].text == 'Length / Beam' and param_cells[1].text != '-':
					vessel_info['Length'] = param_cells[1].text.split('/')[0].strip()
					vessel_info['Beam'] = param_cells[1].text.split('/')[1].strip()
				elif param_cells[0].text == 'Current draught':
					vessel_info['Current draught'] = param_cells[1].text.strip()
				elif param_cells[0].text == 'Course / Speed' and param_cells[1].text != '-':
					vessel_info['Course'] = param_cells[1].text.split('/')[0].strip()
					vessel_info['Speed'] = param_cells[1].text.split('/')[1].strip()
				elif param_cells[0].text == 'Coordinates':
					vessel_info['Coordinates'] = param_cells[1].text.strip()
				elif param_cells[0].text == 'Last report':
					vessel_info['Last report'] = param_cells[1].text.strip()
				else:
					pass

	vessels.append(vessel_info)

driver.close()
print("Elapsed time: %s seconds..." %(time.time() - start_time))

## Write vessel parameters to file
print("Write to csv file...")
vessels_df_cols = ['IMO No.', 'AIS Type', 'Flag', 'Destination', 'ETA', 'MMSI', 'Callsign', 
				'Length', 'Beam', 'Current draught', 'Course', 'Speed', 'Coordinates', 'Last report']
vessels_df = pd.DataFrame(vessels, columns=vessels_df_cols)
vessels_df.to_csv('vessels.csv', index=False, encoding="utf-8")

