import json

def main():
    with open('teacher.json') as file_data:
        data = json.load(file_data)
        newApeals = False
        for month in data["month"]:
            if (month["apeal"]) == "20":
                with open('student.json') as file_data:
                    data = json.load(file_data)
                    for student in data["student"]:
                        if (month["day"]) == (student["student that apealed dates"]):
                            print(" we want to inform that exam was taken down by you students")
                            data["student that apealed dates"].append({(month["day"]) == (student["student that apealed dates"])})

                    file = open("student.json", "w")
                    file.write(json.dumps(data, indent=2))
                    file.close()

        if (newApeals == False):
            print("nothing new happened students")