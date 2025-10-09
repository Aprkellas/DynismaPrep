from ingest import parse_telemetry
import os

def main():
    file_path = input("Enter the path to the telemetry file: ")
    
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        print("Invalid file path. Please try again.")
        return
    
    df = parse_telemetry(file_path)
    print(df.head())


if __name__ == "__main__":
    main()