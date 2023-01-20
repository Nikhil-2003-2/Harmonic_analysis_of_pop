from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from csv import writer
import pandas as pd
import time
pathfile = open("path.txt", mode='r', encoding='utf-8')
path = pathfile.read()
driver = webdriver.Chrome(path)
pathfile.close()
data = pd.read_csv('new.csv', index_col=None)
name = data['Song_Name'].to_list()
artist = data['Artist_Name'].to_list()
link = data['Song_link'].tolist()
driver.get("https://tunebat.com/")
time.sleep(5)
f = open("error.csv", "a+")
for i in range(len(name)):
    with open('new1.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        try:
            search = driver.find_element(
                "xpath", "//input[starts-with(@class, 'ant-input ant-input-lg')]")
            search.send_keys(name[i]+" "+artist[i])
            search.send_keys(Keys.RETURN)
            time.sleep(4)
            key = driver.find_elements(
                "xpath", "//p[starts-with(@class, 'lAjUd')]")
            # print(key[0].text)

            # bpm = driver.find_element(
            #     "xpath", "//p[starts-with(@class, 'lAjUd')]")
            # print(key[1].text)
            row = []
            row.append(name[i])
            row.append(artist[i])
            row.append(key[0].text)
            row.append(key[1].text)
            # row.append(song_link[i].get_attribute('href'))
            csv_writer.writerow(row)
            # time.sleep(5)
        except Exception as e:
            f.write(name[i]+" "+artist[i]+" " + link[i] + "\n")
            print("Error!!!!")

driver.quit()
