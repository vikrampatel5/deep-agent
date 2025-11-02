import os
from dotenv import load_dotenv

from calc_agent import call_calc_agent
from todo_agent import call_todo_agent

load_dotenv(os.path.join(".", ".env"), override=True)

def main():
    call_calc_agent()
    print("-------------------------------")
    call_todo_agent()

if __name__ == "__main__":
    main()
