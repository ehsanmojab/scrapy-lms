import scrapy
from scrapy.http import FormRequest
import pandas as pd

class StidSpider(scrapy.Spider):
    name = "stid"
    allowed_domains = ["lms2.usb.ac.ir"]
    start_urls = ["https://lms2.usb.ac.ir"]
    csv_file_name = 'stid.csv'

    max_id = 8300
    username = ""
    password = ""
    
    fullname = []
    fullid = []
    stuid = []
    ID = []

    def parse(self, response):
        login_token = response.css('input[name="logintoken"]::attr(value)').get()
        yield FormRequest.from_response(response,
                                    formid='login', # fill username and password
                                    formdata={'username': self.username, 'password': self.password, 'logintoken': login_token},
                                    callback=self.after_login)


    def after_login(self, response):
        s = str(response.css('a::text').getall())
        id = 1
        while id < self.max_id:
            yield scrapy.Request(url=f'https://lms2.usb.ac.ir/user/profile.php?id={id}', callback=self.get_id)
            id += 1

        


    def get_id(self, response):
        stid = str(response.css('.card-body ul dl dd a::text').getall())
        h1 = str(response.xpath('//h1/text()').get())

        stid1 = stid[3:stid.find('@')]

        h1 = h1.replace('ك','ک')
        h1 = h1.replace('ي','ی')

        self.fullname.append(h1)
        self.stuid.append(stid1)
        self.fullid.append(stid[2:len(stid)-2])
        self.ID.append(str(response)[str(response).find('=')+1:len(str(response))-1])

        return None

    def close(self):
        df = pd.DataFrame({"fullname":self.fullname,"student id":self.stuid ,"full id":self.fullid, "id":self.ID})
        df.to_csv(self.csv_file_name)
        print("*"*100,'done!')