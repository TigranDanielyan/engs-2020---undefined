import json

def main():
    type = input("do what to start new exam (yes or no) ")
    if type == "yes":
        type = input(" do you want to find a slot or you have a date")

    if type == "find":
        print("found")
    with open('jason.json') as f:
        data = json.load("f")
    for month in data ["month"]:
        if (month["filled"]) == "yes":
            print (month["day"])

    if type == "date":
        type == input ("please enter the day of the exam from 1-31")

    if type == "no":
        print("no")