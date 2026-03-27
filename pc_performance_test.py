import psutil

def main():
    print("==== PC Performance Test Tool ====")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"RAM Usage: {psutil.virtual_memory().percent}%")
    print(f"Total RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
    print(f"Available RAM: {round(psutil.virtual_memory().available / (1024**3), 2)} GB")

if __name__ == "__main__":
    main()