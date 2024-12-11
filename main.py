import os

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

if __name__ == "__main__":
    choice = inquirer.select(
        raise_keyboard_interrupt=False,
        mandatory=False,
        vi_mode=True,
        message="Select Algorithm to Run",
        default=0,
        choices=[
            Choice(0, "FCFS"),
            Choice(1, "SJF"),
            Choice(2, "Priority Non-Preemptive"),
            Choice(3, "Priority Based"),
            Choice(4, "MLQ"),
            Choice(5, "RR"),
        ],
    ).execute()

    if choice == 0:
        os.system("python ./core/fcfs.py")
    elif choice == 1:
        os.system("python ./core/sjf.py")
    elif choice == 2:
        os.system("python ./core/prio-np.py")
    elif choice == 3:
        os.system("python ./core/prio-p.py")
    elif choice == 4:
        os.system("python ./core/mlq.py")
    elif choice == 5:
        os.system("python ./core/roundrobin.py")
