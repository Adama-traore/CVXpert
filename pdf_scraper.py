import os
import csv
from translate import Translator

input_csv_file = 'assets/data/UpdatedResumeDataSet.csv'
output_csv_file = 'output1.csv'

translator = Translator(to_lang='fr')

translated_data = []

with open(input_csv_file, 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)

    for row in csv_reader:
        translated_row = []
        for item in row:
            translated_text = translator.translate(item)
            translated_row.append(translated_text)
        translated_data.append(translated_row)

with open(output_csv_file, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)
    csv_writer.writerows(translated_data)

print(f"Traduction terminée. Les données traduites ont été enregistrées dans {output_csv_file}.")