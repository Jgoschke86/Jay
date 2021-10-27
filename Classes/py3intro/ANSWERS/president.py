
from datetime import date

months = [
    None, 
    'Jan','Feb','Mar','Apr','May','Jun',
    'Jul','Aug','Sep','Oct','Nov','Dec'
]

class President(object):

    def __init__(self,index):
        self._get_data(index)

    @staticmethod
    def _mkdate(year,month,day):
        d = None
        if year != '':
            m = int(months.index(month))
            d = date(int(year),m,int(day))
        return d

    def _get_data(self,index):
        pfile = open("../DATA/presidents.txt")
        for line in pfile:
            flds = line.split(":")
            if int(flds[0]) == int(index):
                self._lname = flds[1]

                self._fname = flds[2]

                self._bdate = self._mkdate(*flds[3:6])
                self._ddate = self._mkdate(*flds[6:9])

                self._bplace = flds[9]
                self._bstate = flds[10]

                self._ts_date = self._mkdate(*flds[11:14])
                self._te_date = self._mkdate(*flds[14:17])

                self._party = flds[17]

                break

        pfile.close()

    @property
    def LastName(self):
        return self._lname

    @property
    def FirstName(self):
        return self._fname

    @property
    def BirthDay(self):
        return self._bdate

    @property
    def DeathDay(self):
        return self._ddate

    @property
    def BirthPlace(self):
        return self._bplace

    @property
    def BirthState(self):
        return self._bstate

    @property
    def TermStart(self):
        return self._ts_date

    @property
    def TermEnd(self):
        return self._te_date

    @property
    def Party(self):
        return self._party

if __name__ == '__main__':
    p = President(1)
    print(p)
    print(dir(p))
    print(p.FirstName, p.LastName)