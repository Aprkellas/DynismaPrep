import os
import asyncio
from ingest import Ingest

def main():
    file_path = input("Enter the path to the telemetry file: ")
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        print("Invalid file path. Please try again.")
        return
    Ingest_instance = Ingest(file_path)
    asyncio.run(Ingest_instance.run_simulation())

if __name__ == "__main__":
    main()