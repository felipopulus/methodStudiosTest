import logging


class TempTracker(object):
    """
    A temperature-tracking class
    """
    def __init__(self, init_temp=None):
        """
        Constructor method
        :param init_temp: optional initial temperature
        """
        # self.logger = logging.log(self.__class__)
        self.__allowedTypes = (int, )  # if float type is desired allowed type, please add it here
        self.__tempList = []
        if init_temp is not None:
            self.insert(init_temp)

    def __repr__(self):
        """
        Overloaded object function that displays the list of
        temperatures in addition to the memory address
        :return: string representation of this object.
        """
        memory_address = super(TempTracker, self).__repr__()
        return "%s %s" % (memory_address, str(self.__tempList))

    def __print_unspuported_type(self, new_item):
        """
        Print unsupported item type. Ex: float values
        :param new_item: the object that is unsupported
        :return: None
        """
        logging.error("Unsupported Type: %s -- Allowed Types: %s" % (type(new_item), self.__allowedTypes))

    def __print_value_error(self):
        """
        When there are no temperature items inserted, this will warn the users
        :return:
        """
        logging.warn("Please insert with at least one temperature item")

    @property
    def temperatures(self):
        """
        Getter property function for object's temperatures
        :return: list of temperatures
        """
        return self.__tempList

    def insert(self, new_item):
        """
        Insert items of allowed types
        :param new_item:
        :return:
        """
        if isinstance(new_item, self.__allowedTypes):
            self.__tempList.append(new_item)
        elif isinstance(new_item, (list, tuple, set)):
            valid_type = all(isinstance(item, self.__allowedTypes) for item in new_item)
            if valid_type:
                self.__tempList.extend(list([x for x in new_item]))
            else:
                self.__print_unspuported_type(new_item)
        else:
            self.__print_unspuported_type(new_item)

    def get_max(self):
        """
        Get gets the highest temperature
        :return: int - highest temperature
        """
        try:
            return max(self.__tempList)
        except ValueError:
            print self.__print_value_error()

    def get_min(self):
        """
        Get gets the lowest temperature
        :return: int - lowest temperature
        """
        try:
            return min(self.__tempList)
        except ValueError:
            print self.__print_value_error()

    def get_mean(self):
        """
        Get gets the average temperature
        :return: int - average temperature
        """
        try:
            return sum(self.__tempList) / float(len(self.__tempList))
        except ZeroDivisionError:
            print self.__print_value_error()


if __name__ == "__main__":
    temp_tracker = TempTracker(99)
    temp_tracker.insert(10)
    temp_tracker.insert([15, 16, 110, 10])
    temp_tracker.insert(25.6)  # will generate an error because floats are not supported.


    print "\n"
    print "Print Temperatures: %s" % temp_tracker.temperatures
    print "Get Max: %s" % temp_tracker.get_max()
    print "Get Min: %s" % temp_tracker.get_min()
    print "Get Mean %s" % temp_tracker.get_mean()
