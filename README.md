# Twitter Sentiment Analysis #

## Introduction ##

Sentiment Analysis is a term that you must have heard if you have been in the Tech field long enough. It is the process of predicting whether a piece of information (i.e. text, most commonly) indicates a positive, negative or neutral sentiment on the topic. In this article, we will go through making a Python program that analyzes the sentiment of tweets on a particular topic. The user will be able to input a keyword and get the sentiment on it based on the latest 100 tweets that contain the input keyword.

Sentiment Analysis refers to the use of Natural Language Processing to determine the attitude, opinions and emotions of a speaker, writer, or other subject within an online mention.

***Essentially, it is the process of determining whether a piece of writing is positive or negative. This is also called the Polarity of the content.***

As humans, we are able to classify text into positive/negative subconsciously. For example, the sentence “The kid had a gorgeous smile on his face”, will most likely give us a positive sentiment. In layman’s terms, we kind of arrive to such conclusion by examining the words and averaging out the positives and the negatives. For instance, the words “gorgeous” and “smile” are more likely to be positive, while words like “the”, “kid” and “face” are really neutral. Therefore, the overall sentiment of the sentence is likely to be positive.

A common use for this technology comes from its deployment in the social media space to discover how people feel about certain topics, particularly through users’ word-of-mouth in textual posts, or in the context of Twitter, their tweets.

## Project Description ##

In this project, we have two parts like:
* Front End ( For managing hashtag, user access permission and monitoring visualization )
* Back End ( For managing all the APIs and populating Twitter data and processing )

### 1. Front End : ###
Here, we have three segments like:
* Sign In and Sign Up Page ( Landing Page )
* Twitter Sentiment Analysis Dashbaord
* Admin Panel

#### Sign In and Sign Up Page ( Landing Page ) : ####
User can sign in or register to see the Twitter Sentiment Analysis Dashboard, if user has access to admin then he / she can also manage the admin panel.

![Landing Page](https://drive.google.com/uc?export=view&id=1hVGA-SZOLZJy7n-EqQAA_tssAzV9ab9r)

#### Twitter Sentiment Analysis Dashbaord : ####

Here, user can see all the information and insights related to the specified hashtags in the Hashtag Manager Page which is resides in the Admin Panel.

![Twitter Sentiment Analysis Dashboard](https://drive.google.com/uc?export=view&id=15jWiapG_ia_6oU0dQ9dd7FzN3msLa7R0)

![Twitter Sentiment Analysis Dashboard](https://drive.google.com/uc?export=view&id=1Mt5Kab4rk0T2VSYWO-OCGzrV4Wvjbl8X)

![Twitter Sentiment Analysis Dashboard](https://drive.google.com/uc?export=view&id=19BOuZ1Ur3hYjjc2qqfWZv6R3tkfU2XPq)

#### Admin Panel : ####
Here, user will see two options like:
* Hashtag Configuration
* User Management

In Hashtag Configuration Page, User can see the all the hashtags for populating data from Twitter, User can activate/ deactive hashtag for populating data, User can add a new hashtag and also User can select the operator for populating data. Suppose, list of hashtags are "suicide", "anxiety", "depression", "frustration" and if User select "AND" then it will be searched for "suicide AND anxiety AND depression AND frustration" otherwise it will be searched for "suicide OR anxiety OR depression OR frustration"

![Hashtag Configuration](https://drive.google.com/uc?export=view&id=1NrbhqUmr5JlTivQPDVM8-yLjv636m1H5)
![Hashtag Configuration](https://drive.google.com/uc?export=view&id=14lt_aM4J3icc4gVExU4kxT2248t6-Sfd)

In User Management Page, User can give admin access to any user or User can also demote any User.

![Hashtag Configuration](https://drive.google.com/uc?export=view&id=1BtDtRRTV_VS89NYFc5pPhwiIllwaklJp)

#### CDN Used ####
CDN name                              | Reference
-------------------------------------------|-----------------------------|
Bootstrap 3 | [![Bootstrap](https://img.shields.io/static/v1?label=Bootstrap&message=v3.4.1&color=blue)](https://getbootstrap.com/docs/3.3/)
Jquery | [![Jquery](https://img.shields.io/static/v1?label=Jquery&message=v3.4.1&color=blue)](https://jquery.com/)
Highcharts | [![Highcharts](https://img.shields.io/static/v1?label=Highcharts&message=v3.4.1&color=blue)](https://www.highcharts.com/)
Swal | [![Swal](https://img.shields.io/static/v1?label=Swal&message=v1.0&color=blue)](https://sweetalert.js.org/)

#### Usage ####
Please, go to the frontend folder of this repository then download the code, after that just click on the index.html web page. Please make sure that your backend server is running behind otherwise it won't work. And if you are using any dedicated hostname then go the js folder then change the baseurl accordingly.
You can deploy the code in any server like Apache.

### 2. Back End : ###
***Please go the backend folder of this repository and download the code.***
### Prerequisite : ###
* Python 3 [Click here to download](https://www.python.org/downloads/).


### Packages ###
Package name                              | Reference
-------------------------------------------|-----------------------------|
Flask | [![Flask](https://img.shields.io/static/v1?label=Flask&message=v1.1.1&color=blue)](https://pypi.org/project/Flask/)
Flask-Cors | [![Flask-Cors](https://img.shields.io/static/v1?label=Flask-Cors&message=v3.0.8&color=blue)](https://pypi.org/project/Flask-Cors/)
Flask-Script | [![Flask-Script](https://img.shields.io/static/v1?label=Flask-Script&message=v2.0.6&color=blue)](https://pypi.org/project/Flask-Script/)
pandas | [![Flask-Script](https://img.shields.io/static/v1?label=pandas&message=v1.0.3&color=blue)](https://pypi.org/project/pandas/)
textblob | [![textblob](https://img.shields.io/static/v1?label=textblob&message=v0.15.3&color=blue)](https://pypi.org/project/textblob/)
tweepy | [![tweepy](https://img.shields.io/static/v1?label=tweepy&message=v3.8.0&color=blue)](https://pypi.org/project/tweepy/)
python-dotenv | [![python-dotenv](https://img.shields.io/static/v1?label=python-dotenv&message=v0.12.0&color=blue)](https://pypi.org/project/python-dotenv/)

### Database and Schema : ###
#### Database used : ####
SQLite3
#### Table Schema : ####
Database name : TwitterDB
Table name                              | Schema
-------------------------------------------|-----------------------------|
Users | id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL, email TEXT, phone TEXT, first_name TEXT NOT NULL, last_name NOT NULL, address TEXT, registration_no TEXT, speciality TEXT,is_admin INT DEFAULT 0
Hashtags | id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, hashtag TEXT NOT NULL, is_activated INT DEFAULT 1
TwitterSentimentAnalysis | id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, operation TEXT NOT NULL

#### Usage :  ####
* Step 1 : Change the twitter developer credentials in the .env file which is resides in the app/config folder.
* Step 2 : Create a virtualenv and activate the virtualenv ( optional ).
* Step 3 : Open your Command Promt or Terminal and then follow the below command
`$ pip3 install -r requirements.txt`
`$ python3 wsgi.py run`
* Step 4: Open your terminal again and execute the following command:
```
  curl -X GET 'http://127.0.0.1:5000/twitter-sentiment-analysis/v1/get-twitter-dataset-from-specifed-hashtag?since=2018-01-01&until=2020-01-01&lang=en' \
  -H 'cache-control: no-cache'

 curl -X POST http://127.0.0.1:5000/twitter-sentiment-analysis/v1/analysis \
  -H 'cache-control: no-cache'
```
* Step 5: You can automate this Step 4. If you're using Windows then go to the task scheduler and create a task, if you're using Linux based OS then you can write a cron job and schedule this Step 4.