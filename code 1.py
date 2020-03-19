import student
import teacher

type = input("are you a teacher or student")
if type == "teacher":

    print ("starting teacher operations")
    teacher.main()

if type == "student":

    print ("starting student operations")
    student.main()

