INF601 - Advanced Programming in Python <br />
Nicholas Zimmerman <br />
Mini Project 4<br />

<h1 align="center"> Nick's AI Generated News Website</h1>
<br>
This project starts a website where users can log in and submit headlines
for news articles, which will be written by an AI content generation
model.

### GPT-Neo
This website uses the GPT-Neo AI model to write the articles. This project
can be viewed at https://github.com/EleutherAI/gpt-neo

### Installation

Start by cloning this repository using: <br><br>
`git clone https://github.com/nczimmerman00/nz_INF_601_MiniProject4.git`


### Prerequisites
To install the packages needed to run the website, open a terminal 
(such as command prompt) in the folder where you cloned this repository 
and enter the following command:
<br> <br>
`pip install -r 'requirements.txt`

For the first time starting the website, you need to initialize the
SQLite database. To do this, use the terminal opened for the cloned
repository and run these commands: <br><br>
`python manage.py makemigrations`<br>
`python manage.py migrate`

### Usage

To start the website, use the terminal you opened in the directory 
where this repository was cloned and run the command: <br><br>
`python manage.py -runserver`

A message should pop up giving a link to the website and the port. The
link won't work, and needs /ai_news appended to the end of it. An
example of a working link is 
<br><br>
`http://127.0.0.1:8000/ai_news/`
<br><br>
To access the admin side of the website, append /admin to the end of the
given link. An example of a working admin link is 
<br><br>
`http://127.0.0.1:8000/admin/`

In order to create an admin user, enter the following command into the 
terminal to initiate a dialog to create an admin user login. 
<br><br>
`python manage.py createsuperuser`
