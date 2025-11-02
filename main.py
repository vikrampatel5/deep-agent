import os
from dotenv import load_dotenv

from agent import process

load_dotenv(os.path.join(".", ".env"), override=True)

def main():
    process()

if __name__ == "__main__":
    main()
