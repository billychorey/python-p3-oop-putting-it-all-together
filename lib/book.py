from ipdb import set_trace

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    
    @property
    def page_count(self):
        return self._page_count
   
    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            #setter assign from an instance.
            self._page_count = value
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        print('Flipping the page...wow, you read fast!')
        
        

# book = Book("Title", "Not an integer")
# book.set_page_count(book.page_count) -not needed bc test doing already


# look up underscore and private

# self is instance each indiv.
# init is instantiating 
# instantiation is creating objects of the class.
# class Students:
#     pass
# Billy=Students() creating an object of the class.
# John=Students() 
# Steve=Students() now we have one class three objects

# if we need to test/flag - do not do in init, do in later test
# if we want to control do not do in init, do in sep methods

# know def of instantiating     vs what python looks for - tasks
#     getter method here: trying to retrieve and return
    
#  look up getter and setter
#     what to do if I need to get