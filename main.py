import threading
from threading import Thread
from elevator import myElevator


elevator = myElevator()
MAX_FLOOR = 15


def main():
    cf = input("enter current floor of elevator:\n").strip()
    elevator.set_current_floor(int(cf))
    my = threading.Thread()

    for i in range(MAX_FLOOR):
        elevator.request.append(['F', -1])

    while True:
        req = input("enter requests:\n").strip()
        dest = input("enter destinations:\n").strip()
        elevator.set_request(int(req)-1, int(dest)-1)
        if not my.is_alive():
            my = threading.Thread(target=elevator.activate, daemon =True)
            my.start()

    # 'T': true -> waiting for elevator
    # 'F': false -> not waiting
    # 'P' pending -> on elevator




if __name__ == "__main__":
    main()
