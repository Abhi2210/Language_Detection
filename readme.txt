===========================================================================
MOdel Training and Generating Model
___________________________________________________________________________
1) Opensource Language.csv is used to train the model
2) Language.csv contains Fields["Text","languange"] which is used as data and labels
3) the generated model is saved as pickle file. 

===========================================================================
Flask Application: 
___________________________________________________________________________
1) Load the pickle file and vector file to conver the text into vectr form.
2) Predicts the language type and accuracy of the model
3) if the score is low its possible the text is less or the lauguange might
 not be the one that is supported. So send the message 
4) Basic error handling if there is error in loading the file and input format is off.
 Those are the only external factor that might throw error

===========================================================================
Testing the api from the Postman: 
___________________________________________________________________________
curl -i -H "Content-Type: application/json" -X POST -d '{"text": "Le parole est l\u0027ombre du fait"}'

