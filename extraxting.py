import yaml
import re
import random
import webscrap_google
questions = []
answers = []

files = ['ai','botprofile','computers','conversations','emotion','food','gossip','greetings','health','history','humor','literature','money','movies','politics','psychology','science','sports','trivia']

for f in files:
    url = "F:/chatterbot-corpus/chatterbot_corpus/data/english/{}.yml".format(f)
    #print(url)
    file = open(url)
    data = yaml.load(file)
    qa = data['conversations']
    
    for i in range(len(qa)):
        questions.append(qa[i][0])
        answers.append(qa[i][1])
        
def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"[-()\"#/@;:<>{}+=~|.?,]", "", text)
    return text

# Cleaning the questions
clean_questions = []
for question in questions:
    clean_questions.append(clean_text(question))

# Cleaning the answers
clean_answers = []
for answer in answers:
    clean_answers.append(clean_text(answer))
    

visited_questions = []
for ques in clean_questions:
    if ques not in visited_questions:
        visited_questions.append(ques)

qa = {}

for ques in visited_questions:
    temp = []
    count = 0
    for index,q in enumerate(clean_questions):
        if ques == q:
            temp.append(clean_answers[index])
            count = count + 1
    qa[ques] = temp

qa['hey'] = ['hi','hello','greetings']
qa['thank'] = ['welcome','my pleasure','you are most welcome']
qa['thank you'] = ['welcome','my pleasure','you are most welcome']

def naming():
    print("Chatbot: Hello there..... May I know your name?")
    a = input("Enter name: ")
    a = a.capitalize()
    print("Chatbot: Hello {}, How may I assist you?".format(a))
    return a,0

naming_flag = 1

print("+++++++++++++++++++++++++++++++++++ITDBot++++++++++++++++++++++++++++++++++++++++++++++")

while True:
    if naming_flag:
        name,naming_flag = naming()
    query = input("{}: ".format(name))
    query = clean_text(query)
    if query == "bye" or query == "goodbye" or query == "exit":
        print("Chatbot: {}".format("Thank you for chatting with me...Bye!"))
        break
    elif "ask" in query:
        print("Chatbot: {}".format("Sure"))
    elif "help" in query:
        print("Chatbot: {}".format("I will do my best to help you!"))
    elif query == "":
        print("Chatbot: {}".format("Can you please retype it?"))
    else:
        flag = 1
        if flag:
            for key,value in qa.items():
                if query == key:
                    ans = value
                    index = random.randrange(0,len(ans))
                    ans = ans[index]
                    ans = ans.capitalize()
                    print("Chatbot: {}".format(ans))
                    break
            else:
                flag = 0
        if not flag:
            ans = "I am sorry I dont know that.. I hope these help you!"
            urls = webscrap_google.searching(query)
            print("Chatbot: {}".format(ans))
            print("Here are some results for you: ")
            for u,v in urls.items():
                print("{} - {}".format(u,v))