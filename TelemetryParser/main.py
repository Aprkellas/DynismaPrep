from parser import parse_telemetry

def main():
    file_path = input("Enter the path to the telemetry file: ")

    df = parse_telemetry(file_path)
    print(df.head())


if __name__ == "__main__":
    main()