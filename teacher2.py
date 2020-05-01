import json

def main():
    with open('teacher.json') as file_data:
        data = json.load(file_data)
        newApeals = False
        for month in data["month"]:
            if str(month["apeal"]) == "20":
                month["filled"] = "No"
                month["apeal"] = 0
                print(" we want to inform that exam dates",month["day"]," have been taken down from teacher side")
                newApeals = True


        if (newApeals == False):
            print("nothing new happened teachers")

        file = open("teacher.json", "w")
        file.write(json.dumps(data, indent=2))
        file.close()
