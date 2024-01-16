import pandas


class SchoolAssessmentSystem:
    def __init__(self):
        self.data = None
    
    
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
                self.data = pandas.read_csv("data/merged_class.csv")
                
            elif new_file_path.endswith('.xlsx'):
                self.data_merged.to_excel("data/merged_class.xlsx", index=False) 
                self.data = pandas.read_csv("data/merged_class.xlsx")
                
        except Exception as e:
            print(f"Error transferring data: {e}")
        
            
    def fetch_web_data(self, url):
        try:
            return pandas.read_csv(url)
        except FileNotFoundError:
            print(f"Error: File not found at {self.url}. Please check the file path.")
        except pandas.errors.EmptyDataError:
            print(f"Error: The CSV file at {self.url} is empty.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
            
    def analyze_content(self, class_num, last_sem_url):
        try:
            self.class_data = self.read_file(class_num)            
            self.class_data["Total_score"] = self.class_data[['Math_Score', 'English_Score', 'Science_Score', 'Social_Score']].sum(axis=1)            
            self.class_avg = self.class_data["Total_score"].mean()/4
            
            self.top_scorer_class = self.class_data.nlargest(3, 'Total_score')
            self.top_scorer_dict = self.top_scorer_class[["Name", "Total_score"]].to_dict(orient='records')
            
            self.last_sem_data = self.fetch_web_data(last_sem_url)
            self.last_sem_avg = (self.last_sem_data[['Math_Score', 'English_Score', 'Science_Score', 'Social_Score']].sum(axis=1)).mean()/4
            
            if self.class_avg > self.last_sem_avg:
                self.statement = f"Average Score has improved by {round(self.class_avg - self.last_sem_avg, 4)}"
            else:
                self.statement = f"Average Score has dropped by {abs(round(self.class_avg - self.last_sem_avg, 4))}"
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
            
    def generate_summary(self, class_num):
        print(f"""    Summary Report of {class_num}:
        Class Average: {self.class_avg}
        Last Semester Average: {self.last_sem_avg}
        {self.statement}
    
    Top Students:
        1. {self.top_scorer_dict[0]['Name']} with the Total score of {self.top_scorer_dict[0]['Total_score']}
        2. {self.top_scorer_dict[1]['Name']} with the Total score of {self.top_scorer_dict[1]['Total_score']}
        3. {self.top_scorer_dict[2]['Name']} with the Total score of {self.top_scorer_dict[2]['Total_score']}
        {"-"*50}                                                                                                                
""")