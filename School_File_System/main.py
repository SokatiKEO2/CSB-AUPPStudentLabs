import schoolfilesystem as sfs
import pandas


class_1 = sfs.SchoolAssessmentSystem()
class_1.analyze_content("School_File_System/data/class_1.csv", "https://raw.githubusercontent.com/SokatiKEO2/CSB-AUPPStudentLabs/main/School_File_System/data/class_1_last_sem.csv")
class_1.generate_summary("Class 1")

class_2 = sfs.SchoolAssessmentSystem()
class_2.analyze_content("School_File_System/data/class_2.csv", "https://raw.githubusercontent.com/SokatiKEO2/CSB-AUPPStudentLabs/main/School_File_System/data/class_2_last_sem.csv")
class_2.generate_summary("Class 2")

all_class = sfs.SchoolAssessmentSystem()
all_class.read_file("School_File_System/data/class_1.csv")
all_class.transfer_data("School_File_System/data/class_2.csv")
all_class.analyze_content("School_File_System/data/merged_class.csv", "https://raw.githubusercontent.com/SokatiKEO2/CSB-AUPPStudentLabs/main/School_File_System/data/merged_class_last_sem.csv")
all_class.generate_summary("Merged Class")