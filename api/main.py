# api/main.py

from fastapi import FastAPI
from naturalNumbers import NaturalNumbersSet

app = FastAPI()

@app.get("/extract/{number}")
def extract_number(number: int):
    numbers_set = NaturalNumbersSet()

    try:
        numbers_set.extract(number)
        missing = numbers_set.find_missing()

        return {
            "message": "Número extraído correctamente",
            "missing_number_calculated": missing
        }

    except ValueError as e:
        return {
            "error": str(e)
        }
    
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Uso: python main.py <numero_entre_1_y_100>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        numbers_set = NaturalNumbersSet()
        numbers_set.extract(number)
        missing = numbers_set.find_missing()

        print(f"Número extraído: {number}")
        print(f"Número faltante calculado: {missing}")

    except ValueError as e:
        print(f"Error: {e}")
        