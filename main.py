import re
from elevator import elevator

elevator = elevator()
MAX_FLOOR = 15

def main():
    global elevator

    req = input().strip()
    req = re.split(r'\s+', req)
    
    dest = input("").strip()
    dest = re.split(r'\s+', dest)

    request = []
    for i in range(MAX_FLOOR):
        request.append([False, -1])
    for i in range(len(req)):
        r = int(req[i]) - 1
        request[r] = [True, dest[i]]

    elevator.set_request(request)


if __name__ == "__main__":
    main()