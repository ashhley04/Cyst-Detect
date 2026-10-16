from flask import * 
from flask import Flask,flash, session, render_template, request, redirect
from flask_mysqldb import MySQL
from tensorflow import keras
from keras.preprocessing.image import load_img
import numpy as np
from flask_mail import Mail, Message
from flask_socketio import SocketIO
from transformers import pipeline
from flask import Flask, request, jsonify
from bardapi import Bard  # Import the Bard API

# Initialize the chatbot model
# chatbot = pipeline('text-generation', model='microsoft/DialoGPT-medium')



import os

app = Flask(__name__) 
socketio = SocketIO(app)
app.secret_key = b'_5#A2L"F4Q8z\n\xec]/'


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'healthcaresquad9@gmail.com'
app.config['MAIL_PASSWORD'] = 'Aish&Ana2022'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Joey@2512'  # Updated with your password
app.config['MYSQL_DB'] = 'fightos'
 



model = keras.models.load_model('model.h5')

# # Set your Bard API key
os.environ['_BARD_API_KEY'] = "g.a000nQj-0NhyUmSFkhzEHrT_EdZc55v3b-FbBAi7fS9m9dc067cdw-DGWAHL98I5eufjF3sVpgACgYKAXgSARcSFQHGX2MigAppDlzlXM-631tppmEWUhoVAUF8yKrrLywA1u6Ck7CnIkxlJUAw0076"

# # Define a chatbot function that interacts with Bard API
def generate_bard_response(user_input):
    try:
        bard = Bard()  # Initialize Bard
        response = bard.get_answer(user_input)['content']
        return response
    except Exception as e:
        print(f"Error in chatbot: {e}")
        return "Sorry, something went wrong."


chatbot = pipeline('text-generation', model='microsoft/DialoGPT-medium')

# test_response = chatbot("Hello, how are you?", max_length=50, num_return_sequences=1)
# print(test_response)


mysql = MySQL(app)

@app.route('/')
def index():
    session['loginSts']=False
    if(session['loginSts']==False):
        return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

  
@app.route('/registeruser', methods = ['POST'])
def registerUser():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT email from user ''')
    emailL= cursor.fetchall()
    #print(emailL)
    for t in emailL:
        #print(t[0])
        if(t[0]==email):
            return render_template('register.html', msg="email already registered. Please login")
    else:
        cursor.execute(''' INSERT INTO user VALUES(%s,%s,%s)''',(name,email,password))
        mysql.connection.commit()
        cursor.close()
        flash("Registration Sucessfull !")
        return redirect(url_for('login'))


@app.route('/login')
def login():
    return redirect(url_for('index', _anchor="appointment"))

  
@app.route('/loginuser',methods = ['POST'])  
def loginuser():
    #global loginSts
    email=request.form['email']
    password=request.form['password']

    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT email, password from user ''')
    epL= cursor.fetchall()
    #print(epL)
    for t in epL:
        #print(t[0])
        if(t[0]==email and t[1]==password):
            cursor.close()
            session['email']=email
            session['loginSts']=True
            return redirect(url_for('portal'))
    else:
        flash("Invalid Credentials")
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['loginSts']=False
    return redirect(url_for('index'))

@app.route('/forgetpass')
def forgetpass():
    return render_template('forgetpass.html')


@app.route("/forgetpassemail",  methods = ['POST'])
def forgetpassemail():
    email = request.form['email']
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * from user ''')
    emailL= cursor.fetchall()
    #print(emailL)
    for t in emailL:
        #print(t[1])
        if(t[1]==email):
            msg = Message('Hello from team FightOS !', sender =  'healthcaresquad9@gmail.com', recipients = [email])
            msg.body = "Hey "+t[0] +", your password is - "+ t[2]
            mail.send(msg)
            return render_template('forgetpass.html', msg_txt="email sent") 
    else:
        return render_template('forgetpass.html', msg_txt="enter registerd email id") 

@app.route('/portal')
def portal():
    if(session['loginSts']==True):
        return render_template('portal.html')
    else:
        return redirect(url_for('index'))

@app.route('/uploadimg', methods = ['POST'])
def uploadimg():
    if(session['loginSts']==True):
        email=session['email']
        #session['loginSts']=True
        destination_path=""
        fileobj = request.files['file']
        file_extensions =  ["JPG","JPEG","PNG"]
        uploaded_file_extension = fileobj.filename.rsplit(".",1)[1]
            #validating file extension
        if(uploaded_file_extension.upper() in file_extensions):
            destination_path= f"data/test/{fileobj.filename}"
            fileobj.save(destination_path)
            try:
                cursor = mysql.connection.cursor()
                #inserting data into table image
                cursor.execute(''' SELECT email from image WHERE email = %s''',(email,))
                record=cursor.fetchone()
                if(record == None ):
                    cursor.execute(''' INSERT INTO image (email,image) VALUES(%s,%s)''',(email,fileobj))
                    mysql.connection.commit()
                else:
                    cursor.execute(''' UPDATE image SET image = %s WHERE email= %s''',(fileobj,email))
                    mysql.connection.commit()
                
                flash('Image successfully uploaded')

                output= predictClass(destination_path)

                if(output=="detected"):
                    if not(os.path.exists(f"data/test/infected/{fileobj.filename}")):
                        os.rename(destination_path,f"data/test/infected/{fileobj.filename}")
                else:
                    if not(os.path.exists(f"data/test/notinfected/{fileobj.filename}")):
                        os.rename(destination_path,f"data/test/notinfected/{fileobj.filename}")

                #print(output)
                #print("predicion done ************")
                
                cursor.close()
                return render_template('portal.html', prediction_text='PCOS - {}'.format(output))
                #return redirect(url_for('portal'))
            except Exception as error:
                #using flash function of flask to flash errors.
                flash(f"{error}")
                return redirect(url_for('portal'))
        else:
            flash("Only images are accepted (png, jpg, jpeg, gif)")
            return redirect(url_for('portal')) 
    else:
        return redirect(url_for('index'))
    



def predictClass(destination_path):

    image = load_img(destination_path, target_size=(224, 224))
    img = image.resize((224, 224))
    img = np.array(image)
    img = img / 255.0
    img = img.reshape(1,224,224,3)
    prediction = model.predict(img)
    l={"Detected":prediction[0][0],"Not Detected":prediction[0][1]}
    j=prediction.max()
    return get_key(j,l)


def get_key(val,l):
    for key, value in l.items():
         if val == value:
             return key
 
    return "Upload a valid ultra sound image"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')  # Get the message from the request
    if not user_input:
        return jsonify({"response": "Please provide a valid message."})

    try:
        # Generate a response using the chatbot model
        response = chatbot(user_input, max_length=100, num_return_sequences=1, truncation=True)
        return jsonify({"response": response[0]['generated_text']})  # Return the response as JSON
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"response": "Sorry, something went wrong. Please try again."})



@app.route('/video-call')
def video_call():
    return render_template('video_call.html')

# @socketio.on('offer')
# def handle_offer(offer):
#     socketio.emit('offer', offer, broadcast=True)

# @socketio.on('answer')
# def handle_answer(answer):
#     socketio.emit('answer', answer, broadcast=True)

# @socketio.on('candidate')
# def handle_candidate(candidate):
#     socketio.emit('candidate', candidate, broadcast=True)




# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.json.get('message')
#     try:
#         response = chatbot(user_input, max_length=100, num_return_sequences=1, truncation=True)
#         return jsonify({"response": response[0]['generated_text']})
#     except Exception as e:
#         print(f"Error occurred: {e}")  # Log the error
#         return jsonify({"response": "Sorry, something went wrong. Please try again."})



 


# if __name__ == '__main__':
#     app.run(port=5028)  # Run the app on port 5001
if __name__ == "__main__":
    app.run(debug=True, port=8080)
