from selenium import webdriver
import pandas as pd

class DowntownHotels:

    path = './chromedriver'

    def __init__(self):

        # assigning selenium webdriver object.
        self.driver = webdriver.Chrome(executable_path=DowntownHotels.path)

        # url we want to open.
        self.url = "https://downtowndallas.com/experience/stay/"

        # lists of data like name,area,address.
        self.hotel_name = []
        self.hotel_address = []
        self.hotel_area = []
        self.hotel_num = []
        self.image_urls = []
        self.links = []   # store link of each hotel.

    def fetched_data(self):

        # opens the url.
        self.driver.get(self.url)
        
        # counts all the images.
        images = self.driver.find_elements_by_class_name('place-square__img')
        
        # fetched all the image urls and assinged it into list
        for image in images:   
            self.image_urls.append(image.find_element_by_tag_name('img').get_attribute('src'))

        # counts all the hotel on our page.
        hotel_links = self.driver.find_elements_by_class_name('place-square__btn')
        

        # fetch link of all hotels and there names.
        for link in hotel_links:
            self.hotel_name.append(link.text)
            self.links.append(link.get_attribute('href'))

        # print(len(self.hotel_name))
        # print(len(self.links))

       # Here we open page of each hotel and get details of it.
        for link in self.links:
            
            # open each hotel link to get data of hotels.
            self.driver.get(link)

            # count the total desired details present.
            hotel_details= self.driver.find_elements_by_class_name('place-info-address')

            # iterate over all the data of hotel.
            for data in range(len(hotel_details)):
                if data == 0:
                    self.hotel_address.append(hotel_details[data].text)
                elif data == 1:
                    self.hotel_num.append(hotel_details[data].text)
                else:
                    self.hotel_area.append(hotel_details[data].text)

            # back to our actual page.(clear this history nad return back)
            self.driver.back()


        # print(self.hotel_name)
        # print(self.hotel_address)
        # print(self.hotel_area)
        # print(self.hotel_num)

    def get_csv(self):

        # dictionary of hotel data.
        hotel_dictionary = {'Name':self.hotel_name,'Address':self.hotel_address,'Street Area':self.hotel_area,'Contact Detail':self.hotel_num,'Image URL':self.image_urls}
        
        # make a dataframe.
        df = pd.DataFrame.from_dict(hotel_dictionary,orient='index')

        print(df)

        df.to_csv('hotel_data.csv')


        



        
   

downtown = DowntownHotels()   
downtown.fetched_data()
downtown.get_csv()