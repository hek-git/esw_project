from Singleton import Singleton
from BubblePool import BubblePool
from Bubble import Bubble

class BubbleManager(Singleton):
    def __init__(self):
        print("버블 매니저 생성")
        self.bubble_pool = BubblePool(20)

    def create_bubble(self):
        print("버블 10개추가생성")
        for i in range(10):
            self.bubble_pool.bubble.append(Bubble())

    def get_bubble(self):
        print("pool에 남은 버블", len(self.bubble_pool.bubble)-1)
        return self.bubble_pool.bubble.pop(0)

    def put_bubble(self, bubble):
        self.bubble_pool.bubble.append(bubble)
        print("pool에 남은 버블", len(self.bubble_pool.bubble))


    def mov_bubble(self, bubble):
        for b in bubble:
            if b.move_count==20:
                b.move_count=0
                self.put_bubble(bubble.pop(0))
            elif b.direction == "right":
                b.position[0] +=3
                b.position[2] +=3
                b.move_count+=1
            else:
                b.position[0] -=3
                b.position[2] -=3
                b.move_count+=1