from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
from csv import writer
import pandas as pd
pathfile = open("path.txt", mode='r', encoding='utf-8')
path = pathfile.read()
driver = webdriver.Chrome(path)
pathfile.close()


def getsongname():
    # time.sleep(1)
    try:
        song_name = driver.find_element("xpath",
                                        "//h1[starts-with(@class, 'dUjZr')]")
        return song_name.text
    except NoSuchElementException as e:
        print(e)
        print('company not found')
        raise TypeError("company not found")


# def getTunning():
#     # time.sleep(1)
#     try:
#         song_name = driver.find_element("xpath",
#                                         "//a[starts-with(@class, 's8LO5')]")
#         Tunning = song_name.text.split()

#         return Tunning
#     except NoSuchElementException as e:
#         print(e)
#         print('company not found')
#         raise TypeError("company not found")


def getkey():
    try:
        song_details = driver.find_elements("xpath",
                                            "(//td[starts-with(@class, 'IcoWj')])")
        song_headers = driver.find_elements("xpath",
                                            "//th[starts-with(@class, 'ZvOWv')]")
        temp = {"Key:": "Key Not Find", "Capo:": "capo Not Find"}
        for song_header, song_detail in zip(song_headers, song_details):
            print(song_header.text)
            if (song_header.text == "Key:"):
                temp[song_header.text] = song_detail.text
            if (song_header.text == "Capo:"):
                temp[song_header.text] = song_detail.text

        # Tunning = song_name[2].text
        # return song_name[2].text
        # print(song_name.text)
        return temp
    except NoSuchElementException as e:
        # print(e)
        print('Key Not Find')
        # return "KNF"
        # raise TypeError("company not found")


def getcapo():
    try:
        song_name = driver.find_elements("xpath",
                                         "(//td[starts-with(@class, 'IcoWj')])")

        return song_name[3].text
    except NoSuchElementException as e:
        print(e)
        print('company not found')
        raise TypeError("company not found")


def getchords():
    try:
        song_name = driver.find_elements("xpath",
                                         "//header[starts-with(@class, 'Ufuqr')]")
        s = ""
        for x in song_name:
            s = s + x.text+" "
        # s = s[:-1]
        temp = s.split()
        return temp
    except NoSuchElementException as e:
        print(e)
        print('company not found')
        raise TypeError("company not found")


def getfreq():
    try:
        song_name = driver.find_elements("xpath",
                                         "//span[starts-with(@class, 'fciXY _Oy28')]")
        s = dict()

        for x in song_name:
            # print(x.text)
            if (s.get(x.text) == None):
                s[x.text] = 0
            s[x.text] = s.get(x.text)+1
        # s = s[:-1]
        # temp = s.split()
        return s
    except NoSuchElementException as e:
        print(e)
        print('company not found')
        raise TypeError("company not found")


def getBpm():
    try:
        song_name = driver.find_element("xpath",
                                        "//span[starts-with(@class, 'WbJde')]")
        # s = dict()
        # print(song_name.text)
        # for x in song_name:
        #     # print(x.text)
        #     if (s.get(x.text) == None):
        #         s[x.text] = 0
        #     s[x.text] = s.get(x.text)+1
        # s = s[:-1]
        # temp = s.split()
        return song_name.text
    except NoSuchElementException as e:
        # print(e)
        return "NF"
        # print('company not found')
        # raise TypeError("company not found")


data = pd.read_csv('link.csv', index_col=None)
links = data['link'].tolist()
f = open("error.csv", 'a+')
for link in links:
    try:
        driver.get(link)
        time.sleep(5)
        with open('new1.csv', 'a+', newline='') as write_obj:
            csv_writer = writer(write_obj)
            row = []
            row.append(getsongname())
            temp = getkey()
            row.append(temp["Key:"])
            row.append(temp["Capo:"])
            row.append(getchords())
            row.append(getfreq())
            row.append(getBpm())
            csv_writer.writerow(row)
    except Exception as e:
        f.write(link)
        f.write("\n")
        print(str(e)+"**")
driver.quit()
driver.quit()
