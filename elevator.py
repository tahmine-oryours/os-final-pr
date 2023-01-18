from time import sleep

MAX_FLOOR = 15

class myElevator:
    def __init__(self):
        self.cur_floor = 0
        self.request = []

    def set_request(self, request):
        self.request = request
    
    def set_current_floor(self, floor):
        self.cur_floor = floor - 1

    def move(self, dest):
        if(self.cur_floor == dest):
            print(f"elevator on floor {self.cur_floor + 1}")
            self.unmount()
            self.mount()
        while(self.cur_floor != dest):
            self.cur_floor += 1 if self.cur_floor < dest else -1
            print(f"elevator on floor {self.cur_floor + 1}")
            self.unmount()
            self.mount()
            sleep(0.5)

    def mount(self):
        if self.request[self.cur_floor][0] == 'T':
            print(f"getting on elevator in floor {self.cur_floor + 1}")
            self.request[self.cur_floor][0] = 'P'
            sleep(0.5)

    def unmount(self):
        for r in self.request:
            if r[0] == 'P' and int(r[1]) == self.cur_floor:
                print(f"getting off elevator in floor {self.cur_floor + 1} from floor {self.request.index(r) + 1}")
                r[0] = 'F'
                sleep(0.5)

    def activate(self):
        direction = self.find_direction()
        self.move(self.cur_floor)

        while(True):
            dest = self.find_dest(direction)
            self.move(dest)
            dest = self.find_mounted_dest(direction)
            self.move(dest)
            if(self.check_finish()):
                break
            direction = self.change_direction(direction)

        print("done!")

    def find_direction(self):
        up_count = down_count = 0
        for i in range(len(self.request)):
            if self.request[i][0] == 'T':
                if i < self.cur_floor:
                    down_count += 1
                else: up_count += 1

        return 'U' if up_count > down_count else 'D'

    def find_dest(self, dir):
        dest = self.cur_floor
        if dir == 'D':
            for i in range(self.cur_floor):
                if self.request[i][0] == 'T':
                    dest = i
                    break
        elif dir == 'U':
            for i in range(MAX_FLOOR - 1, self.cur_floor, -1):
                if self.request[i][0] == 'T':
                    dest = i
                    break
        return dest

    def find_mounted_dest(self, dir):
        req = self.cur_floor
        for r in self.request:
            if r[0] == 'P':
                if (dir == 'D' and r[1] < req) \
                    or (dir == 'U' and r[1] > req):
                    req = r[1]
        return req

    def change_direction(self, dir):
        print("changing direction...")
        sleep(1)
        return 'U' if dir == 'D' else 'D'

    def check_finish(self):
        finished = True
        for r in self.request:
            if r[0] != 'F':
                finished = False
        return finished


#sleep(3)
