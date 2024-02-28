# Exception Handling und Dateiverarbeitung
def read_file_and_count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            line_word_counts = {line_no+1: len(line.split()) for line_no, line in enumerate(file.readlines())}
        print(line_word_counts)
    except FileNotFoundError:
        print(f"Die Datei {file_name} wurde nicht gefunden.")

read_file_and_count_words('aufgabe_1_info.txt')
read_file_and_count_words('nicht_vorhandene_datei.txt')