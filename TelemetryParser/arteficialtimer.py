import asyncio

class ArteficialTimer:
    def __init__(self):
        self.time = 0
        self.pause = 1
        self.increment = 0.05
        self.running = True

    async def timer (self):
        while self.running:
            await asyncio.sleep(1)
            self.time += self.increment
            # print(f"Timer: {self.time:.2f} seconds")

    def turn_off(self):
        self.running = False
        print("Timer turned off")