# Python-Exercise-Interview-Questions
My solutions to some of the python coding questions I've been asked in Interviews. You have to change the datasources in the python scripts accordingly to make the scripts work.

# TASKS

# Task 1:

The following dataset contains eCommerce clickstream information: https://goo.gl/LqHSnK
Each record in represents an event by a visitor on an eCommerce website, with the following information:

data->clicked_epoch (UNIX timestamp in seconds),
date,
user_id,
product_id,
price,
category

Write a python script to assign a “Session ID” to every record in the data . A Session is a window of activity from a user & it ends when there is at least 15 mins of inactivity.

 

# Task 2:

The following dataset contains transactions data: https://goo.gl/kTnPMn
For every transaction, the following fields have been provided:

data->product_id,
category,
date

For each category in the dataset, find out if there is a seasonal pattern in purchase behaviour. Correspondingly, generate seasonal scores (Range: [0, 1]) for each category across seasons* to indicate seasonal relevance of the category at a given time period.

* Seasons can be constructed as months
