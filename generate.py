import csv
import random
import os
import sys

NUM_ROWS = 50


COLUMNS = ["Марка", "Тип двигателя", "Объем двигателя", "Кол-во лошадинных сил", "Масса в кг"]

def generate_row():

    return {
        "Марка": random.choice(["Феррари", "Ламборгини", "Пагани", "Макларен", "Кенигсег", "Бугатти"]),
        "Тип двигателя": random.choice(["V6", "V8", "V10", "V12", "W16"]),
        "Объем двигателя": round(random.uniform(1.5, 9.9), 1),
        "Кол-во лошадинных сил": random.randint(500, 1500),
        "Масса в кг": random.randint(1000, 2500),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)

