class Entry:

    def __init__(self, item, cat, subcat, breakdown):
        self.__item = item
        self.__cat = cat
        self.__subcat = subcat
        self.__breakdown = breakdown

    def get_item(self):
        return self.__item

    def get_cat(self):
        return self.__cat

    def get_subcat(self):
        return self.__subcat

    def get_breakdown(self):
        return self.__breakdown

    def __str__(self):
        return "Item: {0}\nCategory: {1}\nSubCategory: {2}\nBreakdown:  {3}".format(self.__item, self.__cat, self.__subcat, self.__breakdown)
