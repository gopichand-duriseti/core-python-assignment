patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}]

class Patient:
    def __init__(self,patients,disease):
        self.patients=patients
        self.disease=disease
    def search_patients(self):
        return f'Patient with {self.disease}: {[patient["Name"] for patient in patients if patient["Disease"] == self.disease]}'
p=Patient(patients,input("Search the disease: "))
print(p.search_patients())  
