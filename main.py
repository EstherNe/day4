# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time



def TimerDecorator():

def TimerDecorator(func, *args, **kwargs):
    start = time.time()
    func(args, kwargs)
    end = time.time()
    return start-end




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
