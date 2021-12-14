# Mood Board

A CIS192 Final Project<br/>
Author: Yiwei(Ellen) Yan

## Project Goal
The user can sign in, upload a facial expression picture, type in their generic mood color and a sentence of how they are feeling, on creating the post, model.h5 will predict the mood reflected by the uploaded picture and gpt-3 will generate a unique color code as output. Different mood cards are displayed on the main page. 
</br>

## Instruction
* unzip the submission file
* run code
```
cd moodcard
pip3 install -r requirements.txt
python3 manage.py runserver
```
* You might get Google.auth incompatibility but the code should run just fine.
* The database already has superuser admin, and normal users named: ellen, kyle, mama. Please do not register user under same names, will lead to error
* Do not worry about the ML model. The model is pretrained by author on Google Colab and loaded into the project's "/main" folder
</br>

## Submitted Files: 
* moodcard: django project folder
* emotion-detect.py: the python code which builds the emotion detection model in /web_project/main/model.h5
</br>

## Django Code Structure
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
  - the user can click the color brick in the middle, click "show colors", choose the slider icon from top, pick RGB slider in the dropdown, and type in the generated HEX code to see what the output of GPT-3 is
</br>

## Comment
* Things to improve: 
  * It would be really nice if individual cards can display the special generated color but with python+html only, it is challenging to pass in a variable into html tag; can consider using javascript for filling in this functionality
  * If the user try to access the /cards page and /cardnew page without logging in they see a blank page, but the routing does not take them back to root page.
  * The model is only around 64% accurate when tested against the test data; the training dataset is also small with only 3000-4000 image per emotion. The pictures are zoomed in photos of faces and some training photos are irrelevant (casually found a random pic of warning sign somewhere in happy pictures) So the predictions of the model is not as oftenly correct, unfortunately. 
* Some considerations during the project:
  *  Tested out different models for the emotional detection dataset, e.g https://www.kaggle.com/odins0n/emotion-detection. However, the model stops at 24% accuracy during training in its first 5 epochs out of 30 so it does not seem correct. 
  *  There is massive difference in the amount of training data available for the "fearful" emotion from the original dataset (around 1000 vs normally 3000-4000), so the author took out this emotion entirely in hope to see an improvement in model accuracy, which sadly did not happen. 
  *  Built different user interface to be different from Arun's lecture demo and twitter project
</br>

## Credits:
* https://www.cis.upenn.edu/~cis192/ Arun Kirubarajan - for this awesome semester of learning
* https://www.kaggle.com/aayushmishra1512/emotion-detector/notebook AAYUSH MISHRA - for the model
* https://www.youtube.com/watch?v=RvnpVJApBz8 Very Academy - for managing uploaded image files 
* openai
