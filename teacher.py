import json

def main():
    type = input("do what to start new exam (yes or no) ")
    if type == "yes":
        type = input(" do you want to find a slot or you have a date")
        if type == "find":
            print("found")
            with open('jason.json') as file_data:
                data = json.load(file_data)
                for month in data ["month"]:
                    if (month["filled"]) == "yes":
                        print (month["day"])

        else:
            if type == "date":
                type == input ("please enter the day of the exam from 1-31")

    else:
        if type == "no":
            print("no")
