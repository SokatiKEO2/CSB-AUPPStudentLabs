import pandas


class SchoolAssessmentSystem:
    
    
    def __init__(self):
        self.data = pandas.DataFrame()
    
        
    def process_file(self, file_path):   
        try:            
            with open(file_path, 'r') as file:
                self.data = file.read()
            return self.data
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return None
        
    
    def transfer_data(self, old_file_path, new_file_path):
        try:
            with open(new_file_path, 'a') as file:
                file.write(self.process_file(old_file_path))
        except UnicodeDecodeError:
            print("Error: Could not read file")

    # def fetch_web_data():

    # def analyze_content():

    # def generate_summary():


# Analyze content & display result area
bruh = SchoolAssessmentSystem()
bruh.process_file("lol.xlsx")
bruh.transfer_data(old_file_path="lol.xlsx",new_file_path="new.xlsx")
