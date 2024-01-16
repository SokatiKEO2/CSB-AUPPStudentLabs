import pandas


class SchoolAssessmentSystem:
    
    
    def __init__(self):
        self.data = None
        self.url = "https://github.com/SokatiKEO2/CSB-AUPPStudentLabs/blob/main/Data/old_semester.csv?raw=true"
    
    
    def read_file(self, file_path):
        try:
            if file_path.endswith('.csv'):
                self.data = pandas.read_csv(file_path)
            elif file_path.endswith('.xlsx') or file_path.endswith("xls"):
                self.data = pandas.read_excel(file_path)
            elif file_path.endswith('.txt'):
                with open(file_path, 'r') as file:
                    self.data = file.read()
            else:
                raise ValueError("Unsupported file format")
            return self.data
        except Exception as e:
            print(f"Error reading file: {e}")

    
    def transfer_data(self, new_file_path):
        try:
            self.transfer_data = pandas.read_csv(new_file_path)
            self.data_merged = pandas.concat([self.transfer_data, self.data], ignore_index = True)
            
            if new_file_path.endswith('.csv'):
                self.data_merged.to_csv("data/merged_class.csv", index=False)
            elif new_file_path.endswith('.xlsx'):
                self.data_merged.to_excel("data/merged_class.xlsx", index=False) 
                
        except Exception as e:
            print(f"Error transferring data: {e}")
        
            
    def fetch_web_data(self):
        try:
            self.website_data = pandas.read_csv(self.url)
            return self.website_data
        except FileNotFoundError:
            print(f"Error: File not found at {self.url}. Please check the file path.")
        except pandas.errors.EmptyDataError:
            print(f"Error: The CSV file at {self.url} is empty.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
            
    def analyze_content(self, class_num):
        try:
            class_data = self.read_file(class_num)            
            class_data["Total_score"] = class_data[['Math_Score', 'English_Score', 'Science_Score', 'Social_Score']].sum(axis=1)            
            class_avg = class_data["Total_score"].mean()/4
            top_scorer_class = class_data.nlargest(3, 'Total_score')
            
            return class_avg, top_scorer_class[['StudentID', 'Name', 'Total_score']]
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    # def generate_summary():

bruh = SchoolAssessmentSystem()
bruh.read_file("data/class_1.csv")
bruh.transfer_data("data/class_2.csv")
class_1 = bruh.analyze_content("data/class_1.csv")
class_2 = bruh.analyze_content("data/class_2.csv")

print(class_1[1])
print(class_2[1])
bruh.fetch_web_data()