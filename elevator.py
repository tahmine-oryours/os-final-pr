from time import sleep

class elevator:
    def __init__(self):
        self.cur_floor = 0
        self.request = []

    def set_request(self, request):
        self.request.append(request)

    def move(self, dest):
        while(self.cur_floor != dest):
            self.cur_floor += 1 if self.cur_floor < dest else -1
            self.pickup()
            sleep(0.5)

    def pickup(self):
        pass





#sleep(3)
