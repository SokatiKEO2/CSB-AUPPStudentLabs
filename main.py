import schoolfilesystem as sfs
import pandas


class_1 = sfs.SchoolAssessmentSystem()
class_1.analyze_content("data/class_1.csv", "https://github.com/SokatiKEO2/CSB-AUPPStudentLabs/blob/main/Data/class_1_last_sem.csv?raw=true")
class_1.generate_summary("Class 1")

class_2 = sfs.SchoolAssessmentSystem()
class_2.analyze_content("data/class_2.csv", "https://github.com/SokatiKEO2/CSB-AUPPStudentLabs/blob/main/Data/class_2_last_sem.csv?raw=true")
class_2.generate_summary("Class 2")

all_class = sfs.SchoolAssessmentSystem()
all_class.read_file("data/class_1.csv")
all_class.transfer_data("data/class_2.csv")
all_class.analyze_content("data/merged_class.csv", "https://github.com/SokatiKEO2/CSB-AUPPStudentLabs/blob/main/Data/merged_class_last_sem.csv?raw=true")
all_class.generate_summary("Merged Class")