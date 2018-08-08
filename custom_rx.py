from abc import abstractmethod
import time

class Observer:    
    @abstractmethod
    def on_next(self, value):
        pass

    @abstractmethod
    def on_completed(self):
        pass
    
    @abstractmethod
    def on_error(self, error):
        pass


class Observable:
    def __init__(self, source):
        """
        source is the data that will be processed on this instance of Observable
        __strategy lets us keep track of how this Observable has been instantiated
        """
        self.source = source
        self.__strategy = None
    
    @classmethod
    def interval(cls, interval):
        """
        :arg cls: Gets the current class (Observable)
        :arg interval: Time (in seconds) of delay between 2 events
        """
        instance = cls(int(interval/1000))
        instance.__strategy = instance.__interval_subscribe
        opened_stream = instance
        return opened_stream

    @classmethod
    def of(cls, *source):
        """
        :args *source: Every single argument given in here will be kept in a tuple
        """
        instance = cls(source)
        instance.__strategy = instance.__of_subscribe
        opened_stream = instance
        return opened_stream
 
    def map(self, func):
        """
        Creates a new instance of Observable with a new source corresponding to the old one
        on which we have performed the given function
        """
        mapped = map(func, self.source)
        mapped_stream = Observable(mapped)
        mapped_stream.__strategy = self.__strategy
        return mapped_stream

    def filter(self, func):
        """
        Creates a new instance of Observable with a new source corresponding to the old one
        on which we have applied the given filter
        """
        filtered = filter(func, self.source)
        filtered_stream = Observable(filtered)
        filtered_stream.__strategy = self.__strategy
        return filtered_stream

    def __of_subscribe(self, source, observer):
        '''Implementation of subscribe if the original stream has been set by using Observable.of'''
        for item in source:
            try:
                observer.on_next(item)
            except Error as e:
                observer.on_error(e)
        observer.on_completed()

    def __interval_subscribe(self, source, observer):
        '''Implementation of subscribe if the original stream has been set by using Observable.interval'''
        n = source
        while True:
            try:
                observer.on_next(n)
                time.sleep(source)
                n += 1
            except Error as e:
                observer.on_error(e)
        observer.on_completed()

    def subscribe(self, *args, **kwargs):
        """
        Generic subscribe function.
        Creates a new Observer and call the method corresponding to this Observable's strategy
        """
        observer = Observer()
        if args:
            if issubclass(type(args[0]), Observer):
                observer = args[0]
            else:
                for i in range(len(args)):
                    if i == 0:
                        observer.on_next = args[i]
                    if i == 1:
                        observer.on_error = args[i]
                    else:
                        observer.on_completed = args[i]
        def wrapper(source, observer):
            self.__strategy(source, observer)
        return wrapper(self.source, observer)      
