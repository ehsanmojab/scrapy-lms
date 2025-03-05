# scrapy-lms
<h3>Scrapy spider to collect student IDs from university of Sistan and Baluchestan's LMS website.</h3>
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- ABOUT THE PROJECT -->
## About Project



This is a simple Scrapy project designed to extract data such as <b>student IDs, first names, and last names </b> of students from the University of Sistan and Baluchestan's Learning Management System (LMS) website.

In 2022, the university launched a new version of its LMS website, which serves as a communication platform between students and professors and hosts course materials. However, the old version of the website is still accessible and contains publicly available data, such as student IDs. Note that this old version only includes information for students enrolled before 2022. While this data may seem trivial, it can be used to estimate the number of students enrolled each year based on their IDs.



<!-- GETTING STARTED -->
## Getting Started

   If you're interested in using this project to extract data from your university's LMS website, follow the steps below to get started.

## Prerequisites
   Before you begin, ensure you have the following installed:
   ```
      Python 3.x
      Scrapy (install using pip install scrapy)
      Pandas (install using pip install pandas)
   ```

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/ehsanmojab/scrapy-lms
   ```
   Alternatively, you can download the code as a ZIP file.
   
2. Install the required Python packages:
   ```sh
   pip install scrapy pandas
   ```
3. Update the `stid.py` file:
   Open the stid.py file located in the lms/spiders directory.

   Replace the USERNAME and PASSWORD variables with valid credentials. You can use one of the username-password pairs from the usernames.csv file (note: the usernames and passwords in this file are identical).
   note: be aware if you want to run this spider on other LMS websites, you can you your own user and password!

Update the START_URL variable with the target LMS website's URL.
4. Run the spider:
   Navigate to the project directory and start the spider using the following command:
   ```sh
   scrapy crawl stid
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>
