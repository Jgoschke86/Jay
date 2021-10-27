
class Media(object):
    
    def __init__(self,title):
        self.Title = title
    
    @property
    def Title(self):
        return self._title
    
    @Title.setter
    def Title(self,title):
        self._title = title