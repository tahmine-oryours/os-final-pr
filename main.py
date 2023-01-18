import re
from elevator import myElevator

elevator = myElevator()
MAX_FLOOR = 15

def main():

    cf = input("enter current floor of elevator:\n").strip()
    elevator.set_current_floor(int(cf))

    req = input("enter requests:\n").strip()
    req = re.split(r'\s+', req)
    
    dest = input("enter destinations:\n").strip()
    dest = re.split(r'\s+', dest)

    request = []
    # 'T': true -> waiting for elevator
    # 'F': false -> not waiting
    # 'P' pending -> on elevator
    for i in range(MAX_FLOOR):
        request.append(['F', -1])
    for i in range(len(req)):
        r = int(req[i]) - 1
        d = int(dest[i]) - 1
        request[r] = ['T', d]

    elevator.set_request(request)
    elevator.activate()


if __name__ == "__main__":
    main()