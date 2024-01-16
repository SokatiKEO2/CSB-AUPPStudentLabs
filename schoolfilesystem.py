import pandas
import urllib.request

class SchoolAssessmentSystem:
    
    
    def __init__(self):
        self.data = pandas.DataFrame()
    
    
    def read_file(self, file_path):
        try:
            if file_path.endswith('.csv'):
                self.data = pandas.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                self.data = pandas.read_excel(file_path)
            elif file_path.endswith('.txt'):
                with open(file_path, 'r') as file:
                    self.data = file.read()
            else:
                raise ValueError("Unsupported file format")
        except Exception as e:
            print(f"Error reading file: {e}")

    
    def transfer_data(self, new_file_path):
        try:
            self.transfer_data = pandas.read_csv(new_file_path)
            self.data_merged = pandas.concat([self.transfer_data, self.data], ignore_index = True)
            print(self.data_merged)
            if new_file_path.endswith('.csv'):
                self.data_merged.to_csv("data/merged_data.csv", index=False)
            elif new_file_path.endswith('.xlsx'):
                self.data_merged.to_excel("data/merged_data.xlsx", index=False) 
        except Exception as e:
            print(f"Error transferring data: {e}")
        
            
    def fetch_web_data(self, url):
        self.website_data = pandas.read_csv(url)
        print(self.website_data)
    # def analyze_content():

    # def generate_summary():

bruh = SchoolAssessmentSystem()
bruh.read_file("data/class_1.csv")
bruh.transfer_data("data/class_2.csv")
bruh.fetch_web_data("https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/people/people-100.csv")