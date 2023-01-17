from time import sleep

class myElevator:
    def __init__(self):
        self.cur_floor = 0
        self.request = []

    def set_request(self, request):
        self.request = request

#### must print/mount/unmount on current floor before moving ####
    def move(self, dest):
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
                print(f"getting off elevator in floor {self.cur_floor + 1}")
                r[0] = 'F'
                sleep(0.5)



#sleep(3)
