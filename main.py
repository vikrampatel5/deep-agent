import os
from dotenv import load_dotenv

from calc_agent import call_calc_agent
from file_agent import call_file_agent
from sub_agents import call_sub_agents
from todo_agent import call_todo_agent

load_dotenv(os.path.join(".", ".env"), override=True)

def main():
    #call_calc_agent()
    #print("-------------------------------")
    #call_todo_agent()
    # print("-------------------------------")
    #call_file_agent()
    # print("-------------------------------")
    call_sub_agents()

if __name__ == "__main__":
    main()
