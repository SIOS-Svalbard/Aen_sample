#!/usr/bin/python3
# encoding: utf-8


'''
 -- Web interface for exporting a Postgresql search.


@author:     Pål Ellingsen
@deffield    updated: Updated
'''


import os
import sys
import cgi
import cgitb
import uuid
import shutil
import psycopg2
import datetime as dt

columns = ["eventID",
           "parentEventID",
           "cruiseNumber",
           "stationName",
           "eventTime",
           "eventDate",
           "decimalLatitude",
           "decimalLongitude",
           "sampleType",
           "gearType",
           "sampleDepthInMeters",
           "bottomDepthInMeters",
           "bottleNumber",
           "samplingProtocol",
           "sampleLocation",
           "eventRemarks",
           "pi_name",
           "pi_email",
           "pi_institution",
           "recordedBy",
           "sampleType",
           "created",
           "modified",
           "history",
           "source"]

__updated__ = '2019-04-03'


#sys.stdout.buffer.write(b"Content-Type: text/html\n\n")
#cgitb.enable()

form = cgi.FieldStorage()

filters = {"startdate" :'2018-01-01',
        "enddate":dt.date.today().isoformat(),
        "stationname":None,
        "geartype":None,
        "sampletype":None,
        "cruisenumber": None,
        "parenteventid":None,
        "startlat":None,
        "startlon":None,
        "endlat":None,
        "endlon":None,
        "eventids":None}
# set the filters
for key in filters.keys():
    if key in form and form[key].value!='':
        if key=='stationname' or key == 'sampletype' or key=='geartype':
            filters[key]=(form[key].value).split('|')
        elif key=='eventids':
            tmp = (form[key].value).replace(' ','')
            filters[key]= list(map(''.join, zip(*[iter(tmp)]*36))) # split the string into uuid strings
        else:
            filters[key]=form[key].value
        #print(filters[key])


def get_filter(startdate =None,enddate=None,stationname=None,geartype=None,sampletype=None,cruisenumber=None,parenteventid=None,startlat=None,startlon=None,endlat=None,endlon=None,eventids=None):
    return ''' 
        CASE when {startdate} is not NULL 
            THEN eventdate between {startdate} AND  {enddate}
        ELSE TRUE
        END
    AND
        CASE when array_length({stationname},1) > 0
            THEN stationname = ANY({stationname})
        ELSE TRUE
        END
    AND
        CASE when array_length({geartype},1) > 0
            THEN geartype = ANY({geartype})
        ELSE TRUE
        END
    AND
        CASE when array_length({sampletype},1) > 0
            THEN sampletype = ANY({sampletype})
        ELSE TRUE
        END
    AND
        CASE when {cruisenumber} is not NULL 
            THEN cast(cruisenumber as text) LIKE {cruisenumber}
        ELSE TRUE
        END
    AND
        CASE when {parenteventid} is not NULL 
            THEN cast(parenteventid as text) LIKE {parenteventid}
        ELSE TRUE
        END
    AND
        CASE when {startlat} is not NULL 
            THEN decimallatitude between {startlat} AND  {endlat}
        ELSE TRUE
        END
    AND
        CASE when {startlon} is not NULL 
            THEN decimallongitude between {startlon} AND  {endlon}
        ELSE TRUE
        END
    AND
        CASE when array_length({eventids},1) > 0
            THEN eventid in (select cast( unnest({eventids}) as uuid))
        ELSE TRUE
        END
    '''.format(startdate = field(startdate),enddate=field(enddate),stationname=field(stationname,True),geartype=field(geartype,True),sampletype=field(sampletype,True),cruisenumber=field(cruisenumber),parenteventid=field(parenteventid),startlat=field(startlat),startlon=field(startlon),endlat=field(endlat),endlon=field(endlon),eventids=field(eventids,True))


def field(f,arr=False):
    if f==None and not(arr):
        return 'NULL'
    elif f==None and arr:
        return 'ARRAY[]::text[]'
    elif arr:
        tmp = 'array['
        for ii,el in enumerate(f):
            if ii!=0:
                tmp=tmp+",'"+str(el)+"'"
            else:
                
                tmp=tmp+"'"+str(el)+"'"
        tmp = tmp+']'
        return tmp
    else: 
        return "'" + str(f) + "'"

def get_fields(columns):
    temp = [] 
    for c in columns:
        temp.append(c+' AS "'+c+'"')
    return ','.join(temp)

# Open connection to database
conn = psycopg2.connect("dbname=aen_db user=aen_user")
conn.set_session(readonly=True)
cur = conn.cursor()

filter_query = get_filter(**filters)
#print(filter_query)

cur.execute('SELECT distinct((each(other)).key) from aen where '+ filter_query)
other_fields= cur.fetchall()

other_str = []

for o in other_fields:
    other_str.append("other->'" + o[0] + "' AS"+' "' + o[0] + '"')

other_str = ','.join(other_str)

print("Content-Type: text/tsv")
print("Content-Disposition: attachment; filename=AeN_sample_database_export.tsv\n")
#sys.stdout.buffer.write(b"Content-Type: text/html\n\n")

sys.stdout.flush()

# Setting export to tab separated such that Excel likes it better
full_query = 'COPY (SELECT ' + get_fields(columns) + ',' + other_str + 'from aen where ' + filter_query +") TO STDOUT CSV HEADER DELIMITER '\t' "


cur.copy_expert(full_query,sys.stdout.buffer)

cur.close()
conn.close()
