import csv
import os


folder_path = r"C:\Users\Trotter\Neumont\CSC181_ScriptingAndAutomation\Assignments\Automating_Tasks\Students\Students"

def rename_file(folder_path):
    for file in os.scandir(folder_path):
        if file.is_file():
            with open(file.path, "r") as f:
                csv_file = csv.reader(f, delimiter=',')
                for row in csv_file:
                    new_file_name = f"{row[1].replace(" ", "")}_{row[0]}_{row[2]}.csv"
                    
                    if file.name != new_file_name:
                        print(f"{file.name} -> {new_file_name}")
                        
                    new_file_name = os.path.join(folder_path, new_file_name)
            os.rename(file.path, new_file_name)
            
    
rename_file(folder_path)

