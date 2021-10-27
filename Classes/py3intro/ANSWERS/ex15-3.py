#!/usr/bin/Python3

from datetime import date

months = [None,'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

def format_date(d):
    return '{0} {1.day}, {1.year}'.format(months[d.month],d)

while  True:
    entered_lname = input("Enter last name: ")
    if entered_lname.lower() == 'q':
        break
    
    with open('../DATA/presidents.txt') as PRES:
        for line in PRES:
            (term, lname, fname, byear, bmon, bday, dyear, dmon, dday,
             bplace, bstate, tsyear, tsmon, tsday, teyear, temon,
             teday, party)  = line[:-1].split(':')

            bmon = months.index(bmon)
            bdate = date(int(byear),bmon, int(bday))
            display_bdate = format_date(bdate)

            if dyear == '':
                asterisk = '*'
                ddate = date.today()
                display_ddate = ''
            else:
                asterisk = ''
                dmon = months.index(dmon)
                ddate = date(int(dyear), dmon, int(dday))
                display_ddate = format_date(ddate)
     
            age = (ddate - bdate).days/365.25
     
            if entered_lname == lname: 
                print("{0} {1} BORN: {2} DIED: {3} AGE: {4:.0f}{5}".format(fname, lname,
                      display_bdate,display_ddate,age,asterisk))
