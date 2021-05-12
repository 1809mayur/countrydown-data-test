# Here we will extract basic details like address,name from a webite for practice.


from selenium import webdriver
import pandas as pd
import csv

path = './chromedriver'

driver = webdriver.Chrome(executable_path=path)

url = "https://downtowndallas.com/experience/stay/"

driver.get(url)



# all the hotel details are fetching.
links = driver.find_elements_by_class_name('place-square__btn')

hotel_names = []
hotel_links = []
for i in links:
    hotel_names.append(i.text)
    hotel_links.append(i.get_attribute('href'))

# print(hotel_links)
# print(hotel_names)

count = 0
hotel_address = []
hotel_num = []
hotel_area = []
for i in hotel_links:      # this will open all the links and fetch the data and store it into our list.
    driver.get(i)
    elem = driver.find_elements_by_class_name('place-info-address')
    count += 1

    for j in range(len(elem)):
        if j == 1:
           hotel_num.append(elem[j].text)
        elif j == 2:
            hotel_address.append(elem[j].text)
        else:
            hotel_area.append(elem[j].text)
    

    # if count == 3:
    #     break

    driver.back()



details = {'Name':hotel_names,'Address':hotel_address,'Phone':hotel_num,'Area':hotel_area}
print(len(hotel_names))
print(len(hotel_address))
print(len(hotel_num))
print(len(hotel_area))
df = pd.DataFrame.from_dict(details,orient='info')
print(df)
   



# class DowntownExtract:

#     path = './chromedriver'

    # def __init__(self):
    #     # assigning selenium webdriver object to self.driver
    #     self.driver = webdriver.Chrome(executable_path=DowntownExtract.path)

    #     # creating url.
    #     self.url = "https://downtowndallas.com/experience/stay/"



#     def extract_data(self):

#         # chrome driver open the downtown website.
#         self.driver.get(self.url)
#         # xpath for fetching name.

#         # x_path_name = '//section[@class="places"]/div[@class="place-square"]/div[@class="place-sqaure__info place-square__info-bg"]/a'



#         # name_data = self.process_xpath(x_path_name,'',1)
#         # name_data.insert(0,'','URL')


#         # getting list of all the article elements.
#         all_object= self.driver.find_element_by_class_name('place-square')

#         name= []
#         for element in range(len(all_object)):
#             img_element = all_object[element].find_element_by_class_name('place-square__img')
#             name.append((img_element.src))
#         return name



# data = DowntownExtract()

# print(data.extract_data())




