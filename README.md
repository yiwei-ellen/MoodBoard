# Mood Board
------
A CIS192 Final Project<br/>
Author: Yiwei(Ellen) Yan

### Project Goal
The user can sign in, upload a facial expression picture, type in their generic mood color and a sentence of how they are feeling, on creating the post, model.h5 will predict the mood reflected by the uploaded picture and gpt-3 will generate a unique color code as output. Different mood cards are displayed on the main page. 

### Code Structure
- 'admin': access the admin page to the server
- '/': the landing page where the user have the option to the login page and the signup page
- 'login': user login page, can access the sign up page here, if logged in, redirects to '/feed'
- 'logout': returns to the landing page
- 'signup': sign up page, redirects to /feed
- 'cards': the display page, user needs to be logged in to see its contents
  - if not logged in, a refresh leads to login page
  - display posts in reverse chronological order
  - provides a link for logging out
  - allows creation of a new post though hyperlink "Create a Post"
- 'cardnew': create a new card
  - take in a picture, a generic color (red, yellow, green, blue, purple) and a sentence from the user
  - function create_card in views.py used the trained model to predict the emotion on the card, the gpt-3 davinci engine takes in the generic color and the detected emotion to generate a better color code. 
  - after creating the code, the user will be redirected to the cards page where the special color code, the emotion, author and time of the card will be displayed

#### Comment
It will be really nice if individual cards can display the special generated color but with python+html only, it is challenging to pass in a variable into html tag

#### Files: 
web_project: a django project folder
* emotion-detect.py: the python code which builds the emotion detection model in /web_project/main/model.h5

#### Credits:
* https://www.cis.upenn.edu/~cis192/ Arun Kirubarajan
* https://www.kaggle.com/aayushmishra1512/emotion-detector/notebook AAYUSH MISHRA - for the model
* openai
