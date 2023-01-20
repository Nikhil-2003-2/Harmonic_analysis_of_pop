from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
from csv import writer
import pandas as pd
import time
pathfile = open("path.txt", mode='r', encoding='utf-8')
path = pathfile.read()
driver = webdriver.Chrome(path)
pathfile.close()

driver.get("https://www.ultimate-guitar.com/explore?page=31&type[]=Chords")
time.sleep(5)


# search = driver.find_elements(
#   "xpath", "//a[starts-with(@class, 'aPPf7 jtEAE lBssT')]")
# print(search.text)
# print(webdriver.title)


def artistname():
    # time.sleep(1)
    try:
        artist_name = driver.find_elements(
            "xpath", "//a[starts-with(@class, 'aPPf7 jtEAE lBssT')]")
        for names in artist_name:
            print(names.text)
        return artist_name
        # print(song_name.text)
        # return artist_name
    except NoSuchElementException as e:
        print(e)
        print('company not found')
        raise TypeError("company not found")


def songname():
    # time.sleep(1)
    try:
        song_name = driver.find_elements(
            "xpath", "//a[starts-with(@class, 'aPPf7 HT3w5 lBssT')]")
        for names in song_name:
            print(names.text)
        return song_name
        # print(song_name.text)
        # return song_name
    except NoSuchElementException as e:
        print(e)
        print('company not found')
        raise TypeError("company not found")


def songlink():
    # time.sleep(1)
    try:
        song_name = driver.find_elements(
            "xpath", "//a[starts-with(@class, 'aPPf7 HT3w5 lBssT')]")
        for names in song_name:
            print(names.get_attribute('href'))
        return song_name
        # print(song_name.text)
        # return song_name
    except NoSuchElementException as e:
        print(e)
        print('company not found')
        raise TypeError("company not found")


# artistname()
# songname()
# songlink()
for i in range(20):
    name = songname()
    artist_name = artistname()
    song_link = songlink()
    with open('new.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        for i in range(len(name)):
            row = []
            row.append(name[i].text)
            row.append(artist_name[i].text)
            row.append(song_link[i].get_attribute('href'))
            csv_writer.writerow(row)
    link = driver.find_element(
        "xpath", "//a[starts-with(@class, 'UHu_z BvSfz GNapi aPPf7 jtEAE lBssT')]")
    link.click()
    time.sleep(5)


# "UHu_z BvSfz GNapi aPPf7 jtEAE lBssT"
# names += 1
driver.quit()
