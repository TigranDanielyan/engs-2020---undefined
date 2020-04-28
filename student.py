import json

def main():
  type = input("give us your name")
  with open('student.json') as file_data:
    data = json.load(file_data)
    for student in data["student"]:
      if type == (student["name"]):
         type = input("give us your password")
         if type == (student["password"]):
           type = input("do what to see exams dates and cancel exam date (yes or no)? ")
           if type == "yes":
             print("starting showing exam dates")
             with open('jason.json') as file_data:
               data = json.load(file_data)
               for month in data["month"]:
                 if (month["filled"]) == "Yes":
                     if (month["filled"]) == "Yes":
                         print("please check if the dates are good for you to take exam")
                         print(month["day"])
                     type = input("choose the date you want to apeal")
                     with open('student.json') as file_data:
                         data = json.load(file_data)
                         for student in data["student"]:
                             if type != (student["student that apealed dates"]):
                                 if type == (month["day"]):
                                     print("startinng apeal")
                                     month["apeal"] = month["apeal"] + 1
                                     break


                 else:
                     if (month["filled"]) == "No":
                         print("No exames are in progress")
                         break

               file = open("jason.json", "w")
               file.write(json.dumps(data, indent=2))
               file.close()

           if type == "no":
              print("shutdown")
              break