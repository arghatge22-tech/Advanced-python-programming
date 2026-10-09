
import csv
import json

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    with open(csvFilePath, "r", encoding="utf-8") as csvf:
        csvReader = csv.DictReader(csvf)

        for row in csvReader:
            jsonArray.append(row)

    with open(jsonFilePath, "w", encoding="utf-8") as jsonf:
        json.dump(jsonArray, jsonf, indent=4)

csvFilePath = "input.csv"
jsonFilePath = "output.json"

csv_to_json(csvFilePath, jsonFilePath)

print("CSV file successfully converted to JSON.")