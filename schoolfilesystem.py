import pandas


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

    
    def transfer_data(self, old_file_path, new_file_path):
        pass

    # def fetch_web_data():

    # def analyze_content():

    # def generate_summary():

bruh = SchoolAssessmentSystem()
bruh.read_file("data/class_1.csv")
print(bruh.data)
