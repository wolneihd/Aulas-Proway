import time

def contador_segundos(segundos: int):
    for index, segundo in enumerate(range(1,segundos+1)):
        time.sleep(1)
        print(f'contador: {index+1} de {segundos}')

if __name__ == "__main__":
    contador_segundos(5)