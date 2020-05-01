import student
import teacher
import student2
import teacher2


student2.main()
teacher2.main()
type = input("are you a teacher or student ")
if type == "teacher":
    print("starting teacher operations")
    teacher.main()

if type == "student":

    print ("starting student operations")
    student.main()
