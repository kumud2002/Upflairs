from flask import Flask, render_template, request, redirect
import nltk
from nltk.chat.util import Chat, reflections

#######################-------------- Chatbot code --------------------########################

# Rules for chat

rules = [# in the form of tuple
        (r"hello",["hi", "hello"]),
        (r"ac is not working" ,["Pankha chalao", "hummare yaha aesa he hota h"]),
        (r"name",["Kumud Jain","My name is Kumud Jain"]),
        (r"skills?",["Machine Learning","Python","c++"]),
        (r"college",["Jaipur Engineering College and Research Centre","JECRC"]),
        (r"field",["Information Techonology"])]

my_chat_bot = Chat(rules)

#######################-------------- Flask code --------------------########################

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page yahan hai ------"


@app.route('/chat', methods = ['POST', 'GET'])
def chatbot():
    # res = ""
    if request.method == "POST":
        ques = request.form['ask_me']
        print(ques)
        res = my_chat_bot.respond(ques)
        print(res)
        return render_template("mypage.html", response_from_flask = res)
    else:
        return render_template("mypage.html")

app.run(debug= True)