class Devices:
    '''
    Basic device:
    filename - input file
    n_of_pages - pages to work with
    '''
    def __init__(self, filename, n_of_pages) -> None:
        self.filename = filename
        self.pages = n_of_pages

class Printer(Devices):
    '''
    Printer device:
    color - True = print colorful, False = print black and white
    '''
    def __init__(self, filename, n_of_pages, color) -> None:
        super().__init__(filename, n_of_pages)
        self.color = color 
    def to_print(self):
        if self.color:
            mode = 'color'
        else:
            mode = 'black/white'
        print(f'Printing of {self.filename}, {self.pages} pages in {mode}')


class Xerox(Devices):
    '''
    Xerox device:
    color - True = copy colorful, False = print black and white
    n_of_copies - how many copies to make
    '''
    def __init__(self, filename, n_of_pages, color, n_of_copies) -> None:
        super().__init__(filename, n_of_pages)
        self.color = color 
        self.copies = n_of_copies
    def to_copy(self):
        if self.color:
            mode = 'color'
        else:
            mode = 'black/white'
        print(f'Copying of {self.filename}, {self.pages} pages in {mode}, {self.copies} times')


class Scanner(Devices):
    '''
    Scanner device
    '''
    def to_scan(self):
        print(f'Scanning of {self.filename}, {self.pages} pages')
