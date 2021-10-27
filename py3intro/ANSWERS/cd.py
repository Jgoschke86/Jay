
from media import Media
from track import Track

class CD(Media):
    
    def __init__(self,title):
        super().__init__(title)
        self._tracks = []  # will hold Track objects
        
    def AddTrack(self,name,minutes,seconds):
        self._tracks.append(Track(name,minutes,seconds))
        
    @property
    def Tracks(self):
        return self._tracks