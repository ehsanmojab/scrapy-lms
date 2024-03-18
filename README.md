# scrapy-lms
<h3>Scrapy spider to collect student IDs from university of Sistan and Baluchestan's LMS website.</h3>
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- ABOUT THE PROJECT -->
## درباره پروژه      About Project



پروژه ای ساده برای استخراج داده هایی مثل <b>شماره دانشجوی</b> <b> همراه با نام و نام خانوادگی</b> دانشجویان دانشگاه سیستان و بلوچستان با استفاده از scrapy.
از سال ۱۴۰۱ دانشگاه ورژن جدیدی از سایت LMS ارائه شد.این سایت که راه ارتباطی بین دانشجو و استاد است و همچنین محتوا های درسی در آن قرار میگرفت. اما ورژن قبلی این سایت هنوز در دسترس است و میتوان داده های بی ارزشی مانند شماره دانشجویی دانشجویان را دید. البته این سایت فقط حاوی اطلاعات دانشجویان ماقبل ۱۴۰۱ است. ( البته خیلی هم بی ارزش نیست، میشه تعداد دانشجوهای هر سال رو با شماره دانشجویی ها بدست آورد! 😄)



<!-- GETTING STARTED -->
## Getting Started

اگه شما هم علاقه مند هستید که این پروژه رو برای استحراج از سایت دانشگاه خودتون استفاده کنید میتونید از اینجا شروع کنید.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ehsanmojab/scrapy-lms
   ```
   or just download the code!
   
3. Install NPM packages
   ```sh
   npm install scrapy
   npm install FormRequest
   npm install pandas
   ```
4. Chnage information in `stid.py`

   یکی از پسورد هایي که داخل فایل `password.csv` هست رو بردارید.( در این فایل username های اکانت هایی هست که با password آنها یکسان است! 😬)
 سپس جایگزین متغیر های username و password در کد `stid.py` در مسیر ‍`lms/spiders` کنید.
همچنین لینک و دامنه سایت مورد نظر رو جایگزین کنید.
6. Go to project directory and start crawling
   ```sh
   scrapy crawl stid
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>
