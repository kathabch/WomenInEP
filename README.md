# WomenInEP
An NLP approach analyzing European Parliament (EP) debates.

This repository accompanies my Master's Thesis "Do Women Matter? A Natural Language Processing Approach Analyzing European Parliament Debates".
It provides information about how the data used was web scraped, transformed and analyzed. 

Data used: debates of the EP for the period 1st of July 2014 to 10th of November 2022 
(i.e. https://www.europarl.europa.eu/doceo/document/CRE-8-2014-07-01_EN.html)

repository used for web scraping: https://github.com/chozelinek/europarl

The steps taken are visualized in the following flowchart:
![flowchart_13-03-23](https://user-images.githubusercontent.com/118127431/225577518-81c08f3d-5303-4064-b2ef-e1a777b8c304.png)


#### step by step data set creation:
- execute the get_proceeding.py file for the required period: https://github.com/chozelinek/europarl/blob/master/get_proceedings.py
- convert the downloaded html-files to xml: https://github.com/chozelinek/europarl/blob/master/proceedings_xml.py
- use the get_interventions.py file to create a data set that is locally saved as .csv
- join the MEP data (meps_joined_data.csv) to previously created dataframe with: joining mep data to df.ipynb

#### notebooks for data analysis
- word frequencies - general vizs.ipynb: getting an overview of the data set
[- language detection of not translated interventions.ipynb: the attempt of translating the previously not translated interventions (spoiler: didn't work)]
- topic modeling with spaCy.ipynb: topic modeling with spaCy to get an overview of the most important topics discussed within the given data set
- word frequencies - topics.ipynb: analyzing pre-defined topics
[- topic modeling with spaCy - Roe v Wade.ipynb: an attempt to find word patterns within the Roe v. Wade topic]




