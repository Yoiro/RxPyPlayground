import time

from custom_rx import Observable, Observer

class PrintObserver(Observer):

    def on_next(self, value):
        print("Received {0}".format(value))

    def on_completed(self):
        print("Done!")

    def on_error(self, error):
        print("Error Occurred: {0}".format(error))


"""
What works:
source_of = Observable.of(...) OK with 1 Object, OK with 3 functions
source_of.map(fn)
source_of.filter(fn)

.of, .map and .filter can be chained together with expected behaviours.

source_int = Observable.int(...)

.int cannot be chained

Subscribe function is ok for both of those methods
"""

source = Observable.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon") \
    # .map(lambda s: len(s))                                           \
    # .filter(lambda x: x > 4)
# source = Observable.of("Alpha")

# lengths = source.map(lambda s: len(s))

# filtered = source.filter(lambda s: len(s) <= 4)

# source.subscribe(PrintObserver())

source.subscribe(
    lambda value: print("Received {0}".format(value)),
    # lambda error: print("Error Occurred: {0}".format(error)),
    # lambda: print("Done!")
)

# source = Observable.interval(1000)   #       \
#     .map(lambda i: "{0} ".format(i))

# source.subscribe(lambda s: print("A: %s" % s))
# time.sleep(2)
# source.subscribe(lambda s: print("B: %s" % s))

# input("Press any key to quit\n")
