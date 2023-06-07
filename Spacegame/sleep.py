class EventLoopComand():

    def __await__(self):
        return (yield self)


class Sleep(EventLoopComand):

    def __init__(self, seconds):
        self.seconds = seconds
