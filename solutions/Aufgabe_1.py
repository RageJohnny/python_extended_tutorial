import os

# Datenstrukturen und Dateioperationen
info = {
    'name': 'Johannes Georg Larcher',
    'age': 27,
    'languages': ['Deutsch', 'Englisch', 'Italienisch'],
    'has_python_experience': True,
    'has_java_experience': True,
    'has_javascript_experience': True
}

def write_info_to_file(info_dict):
    # Stelle sicher, dass der Ordner 'data' existiert
    os.makedirs('data', exist_ok=True)
    
    # Pfad zum Speichern der Datei im Ordner 'data'
    file_path = 'data/aufgabe_1_info.txt'
    
    with open(file_path, 'w') as file:
        for key, value in info_dict.items():
            file.write(f"{key}: {value}\n")
    print(f"Informationen wurden erfolgreich in {file_path} geschrieben.")

write_info_to_file(info)