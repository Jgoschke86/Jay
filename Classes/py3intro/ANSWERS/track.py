
class Track(object):
    """
    An audio track from some kind of media. 
    """ 
    def __init__(self,name,minutes,seconds,artists=None):
        self._name = name
        self._minutes = minutes
        self._seconds = seconds
        if artists is None:
            self._artists = []
        else:
            self._artists = artists
        
    @property
    def Name(self):
        return self._name

    @property
    def Length(self):
        return "{0:d}:{1:02d}".format(self._minutes,self._seconds)
    
    @property
    def Artists(self):
        return self._artists