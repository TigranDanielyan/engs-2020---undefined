import json

def main():
    type = input("do you what to start new exam (yes or no) ")
    if type == "yes":
        type = input(" do you want to find a slot or you have a date ")
        if type == "find":
            print("empty days are")
            with open('jason.json') as file_data:
                data = json.load(file_data)
                for month in data ["month"]:
                    if (month["filled"]) == "No":
                        print (month["day"])
        else:
            if type == "date":
                with open('jason.json') as file_data:
                    data = json.load(file_data)
                    for month in data["month"]:
                        type = input ("please enter the day of the exam from 1-31 ")
                        if type == (month["day"]):
                            if (month["filled"]) == "Yes":
                                print ("sorry it is taken")
                                with open('jason.json') as file_data:
                                    data = json.load(file_data)
                                    for month in data["month"]:
                                        if (month["filled"]) == "No":
                                            print(month["day"])
                            if (month["filled"]) == "No":
                                month["filled"] = "Yes"
                                print(month["day"])
                                print("registered for you")
                                data = open("jason.json", "w")
                                data.write(json.dumps(month["filled"]))
                                data.close()
                                break
    else:
        if type == "no":
            print("no")
