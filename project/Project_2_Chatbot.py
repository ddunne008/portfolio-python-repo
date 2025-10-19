import random
import time
import datetime
import json

with open("keywords.json", "r") as keyword_file:
    keywords = json.load(keyword_file)

Agents = ["Martha", "Sarah","Dean","Alex","Joseph","Dylan", "Carlos", "Amelia", "Eden"] #This contains a list of Agents in the system
Stop_words = ["exit", "Exit", "Quit", "quit", "Bye", "bye", "Stop", "stop"] #This is a list of stop words which will terminate the program
Course_queries = ["what courses are available?", "What courses are available", "show me courses available"] #This is a list of keywords about course queries
Courses_available = ["Marketing", "IT in Business", "Cyber Security", "Sport Science", "Sport Coaching", "Basket Weaving", "Project Management", "Civil Engineering"] #This is a list of courses that are available
Campus_Cafe_Words = ["campus cafe", "Campus Cafe", "Poppies", "poppies", "is there a cafe on campus", "Is there a cafe on campus", "is there a cafe on campus?"] #This is a list of keywords about the campus cafe
EE_1 = ["Who made this", "who made this", "Who made this Program", "Who made this program?", "who is your creator", "who is your creator?"] #This is a list of keywords about an Easter egg within the program
EE_2 = ["Tell me a fun fact", "fun fact", "Fun fact", "give me a fun fact", "tell me something i dont know"] #This is a list which will print fun facts for the user
EE_2_answers = ["Did you know that an Octopus has 3 hearts?", "If you close your eyes, you wont see this screen", "Counting from 0 - 100, the only time your lips touch is when you say 100", "This is the first Python Project Daniel has even done", "If a vampire cant see itself in a mirror, how do they have such good hairstyles?"] #This is a list which prints to the user


def marketing_course():
    print(agent,">>> Here is the details about the Marketing Course we offer")
    print("************************")
    print("Course Tittle: Bsc Hons")
    print("Course Duration: 3 Years")
    print("Placement Year Available: Yes")
    print("Course Talks: 9:00am - 10:30am")
    print("************************")

def it_business_course():
    print(agent,">>> Here is the details about the IT in Business Course we offer")
    print("************************")
    print("Course Tittle: Bsc Hons")
    print("Course Duration: 3 Years")
    print("Placement Year Available: No")
    print("Course Talks: 14:00pm - 15:30pm")
    print("************************")

def cyber_security_course():
    print(agent,">>> Here is the details about the Cyber Security Course we offer")
    print("************************")
    print("Course Tittle: BEng Hons")
    print("Course Duration: 3 Years")
    print("Placement Year Available: Yes")
    print("Course Talks: 11:00am - 12:30pm")
    print("************************")

def sport_science_course():
    print(agent,">>> Here is the details about the Sport Science Course we offer")
    print("************************")
    print("Course Tittle: Bsc Hons")
    print("Course Duration: 3 Years")
    print("Placement Year Available: No")
    print("Course Talks: 12:30pm - 14:00pm")
    print("************************")

def sport_coaching_course():
    print(agent,">>> Here is the details about the Sport Coaching Course we offer")
    print("************************")
    print("Course Tittle: Bsc Hons")
    print("Course Duration: 3 Years")
    print("Placement Year Available: Yes")
    print("Course Talks: 09:00am - 10:30am")
    print("************************")

def basket_weaving_course():
    print(agent,">>> Here is the details about the Basket Weaving Course we offer")
    print("************************")
    print("Course Tittle: Bsc Hons")
    print("Course Duration: 2 Years")
    print("Placement Year Available: No")
    print("Course Talks: 11:00am - 12:30pm")
    print("************************")

def project_management_course():
    print(agent,">>> Here is the details about the Project Management Course we offer")
    print("************************")
    print("Course Tittle: BEng Hons")
    print("Course Duration: 3 Years")
    print("Placement Year Available: Yes")
    print("Course Talks: 13:45pm - 15:15pm")
    print("************************")

def civil_engineering_course():
    print(agent,">>> Here is the details about the Civil Engineering Course we offer")
    print("************************")
    print("Course Tittle: BEng Hons")
    print("Course Duration: 3 Years")
    print("Placement Year Available: Yes")
    print("Course Talks: 10:00am - 11:30am")
    print("************************")

def campus_cafe_info():
    print(agent,">>> The Campus Cafe, also known as poppies, serves a variety of coffe, tea and homemade smoothies with many snacks! We are a big believer in recycling and doing our part for mother nature, We are open Monday - Saturday, 8am - 16:30pm everyday")

def main_screen(terminal): #This is the first screen the user will see
    terminal = input(">>> ")
    if terminal in Stop_words:
        print(agent,">>> Enjoy the rest of your day!")
        quit() #This code will stop the program when the user enters an exit word from the stop_words list
    if terminal == "":
        return main_screen(terminal)
    if terminal in Campus_Cafe_Words:
        campus_cafe_info()
        return main_screen(terminal)
    if terminal in Course_queries:
        print(agent,">>> Yes", username, " The courses that are available this year are: ", Courses_available, "If you want more Information about a course type in the course tittle")
        return main_screen(terminal)
    if terminal in Courses_available:
        if terminal == "Marketing":
            marketing_course()
            return main_screen(terminal)
        if terminal == "IT in Business":
            it_business_course()
            return main_screen(terminal)
        if terminal == "Cyber Security":
            cyber_security_course()
            return main_screen(terminal)
        if terminal == "Sport Science":
            sport_science_course()
            return main_screen(terminal)
        if terminal == "Basket Weaving":
            basket_weaving_course()
            return main_screen(terminal)
        if terminal == "Project Management":
            project_management_course()
            return main_screen(terminal)
        if terminal == "Civil Engineering":
            civil_engineering_course()
            return main_screen(terminal)
        else:
            print(agent,">>> Im not sure which course you are looking for, please re-type the course name")
            return main_screen(terminal)

    if terminal in EE_1:
        print(agent,">>> Yes, The creator of this program was made by Daniel Dunne, A student at LBU, Although im not sure why hes made a coding system for another rival university...")
        return main_screen(terminal)
    if terminal in EE_2:
        answer = random.choice(EE_2_answers)
        print(agent,">>> Sure", answer)
        return main_screen(terminal)
    else:
        print(agent,">>> Im sorry, I dont understand what your looking for, Maybe re-type the question again or in more detail and I can help more")
        return main_screen(terminal)

#This is the first part of the chatbot system which will display a welcome to the chatbot
print("****Welcome to the University of Poppleton Chatbot System!*****")
print("Current Time:", datetime.datetime.now())
username = input("SYSTEM >>> What is your name: ")
if username == "":
    username = "Stranger"
print("SYSTEM >>> Hello", username,"Good to meet you, give me one moment whilst you are connecting to an agent")


time.sleep(3.5) #This slows down the program to give a realistic suspense


agent = random.choice(Agents) #This assigns a random agent name from the Agents list
terminal = print("SYSTEM >>> Hello", username, ", Agent:", agent, "is connected")
print(agent,">>>", "Hey there,", username,"Nice to meet you! What can I help you with?")
#This generates a unique chat ID which can be used for testing or back-end purposes within the project
agent_no = agent[0]
user_no = username[0]
ran_no = random.randint(100,1000) #The chat ID will take the first letter of the agent and usernames and then generate a random number between 100 and 1000
ran_no = str(ran_no) #This converts the random integer to a string so it can be combined with the code below
chat_id = agent_no + user_no + ran_no
print("Chat ID: ",chat_id)

main_screen(terminal)





