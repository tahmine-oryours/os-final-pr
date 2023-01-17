import re
from elevator import myElevator

elevator = myElevator()
MAX_FLOOR = 15

def main():

    req = input().strip()
    req = re.split(r'\s+', req)
    
    dest = input("").strip()
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



if __name__ == "__main__":
    main()