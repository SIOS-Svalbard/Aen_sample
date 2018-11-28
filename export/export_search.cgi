#!/usr/bin/python3
# encoding: utf-8


'''
 -- Web interface for exproting a Postgresql search.


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
from psycopg2 import sql
import datetime as dt

columns = ["eventID",
           "parentEventID",
           "cruiseNumber",
           "stationName",
           "eventTime",
           "eventDate",
           "decimalLatitude",
           "decimalLongitude",
           "bottomDepthInMeters",
           "eventRemarks",
           "samplingProtocol",
           "sampleLocation",
           "pi_name",
           "pi_email",
           "pi_institution",
           "recordedBy",
           "sampleType",
           "created",
           "modified",
           "history",
           "source"]

__updated__ = '2018-11-28'


# cgitb.enable()

method = os.environ.get("REQUEST_METHOD", "GET")
if method == "GET":  # This is for getting the page
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
            "endlon":None}
    # set the filters
    for key in filters.keys():
        if key in form and form[key].value!='':
            if key=='stationname':
                filters[key]=(form[key].value).split('|')
            else:
                filters[key]=form[key].value
    
    #sys.stdout.buffer.write(b"Content-Type: text/html\n\n")
    #print(filters)

    def get_filter(startdate =None,enddate=None,stationname=None,geartype=None,sampletype=None,cruisenumber=None,parenteventid=None,startlat=None,startlon=None,endlat=None,endlon=None):
        return sql.SQL(''' 
        CASE when {startdate} is not NULL THEN eventdate between {startdate} AND  {enddate}
        ELSE TRUE
        END
        AND
            CASE when ({stationname}) is not NULL THEN stationname = ANY({stationname})
        ELSE TRUE
        END
        AND
        CASE when {geartype} is not NULL THEN geartype ILIKE concat('%',{geartype}, '%')
        ELSE TRUE
        END
        AND
        CASE when {sampletype} is not NULL THEN sampletype ILIKE concat('%',{sampletype},'%')
        ELSE TRUE
        END
        AND
        CASE when {cruisenumber} is not NULL THEN cast(cruisenumber as text) LIKE {cruisenumber}
        ELSE TRUE
        END
        AND
        CASE when {parenteventid} is not NULL THEN cast(parenteventid as text) LIKE {parenteventid}
        ELSE TRUE
        END
        AND
        CASE when {startlat} is not NULL THEN decimallatitude between {startlat} AND  {endlat}
        ELSE TRUE
        END
        AND
        CASE when {startlon} is not NULL THEN decimallongitude between {startlon} AND  {endlon}
        ELSE TRUE
        END''').format(startdate = sql.Literal(startdate),enddate=sql.Literal(enddate),stationname=sql.Literal(stationname),geartype=sql.Literal(geartype),sampletype=sql.Literal(sampletype),cruisenumber=sql.Literal(cruisenumber),parenteventid=sql.Literal(parenteventid),startlat=sql.Literal(startlat),startlon=sql.Literal(startlon),endlat=sql.Literal(endlat),endlon=sql.Literal(endlon))



    def get_fields(columns):
        temp = [] 
        for c in columns:
            temp.append(c+' AS "'+c+'"')
        return ','.join(temp)

    # Open connection to database
    conn = psycopg2.connect("dbname=test user=www")
    conn.set_session(readonly=True)
    cur = conn.cursor()

    filter_query = get_filter(**filters).as_string(conn) 

    cur.execute('SELECT distinct((each(other)).key) from aen where '+ filter_query)
    other_fields= cur.fetchall()

    other_str = []

    for o in other_fields:
        other_str.append("other->'" + o[0] + "' AS"+' "' + o[0] + '"')

    other_str = ','.join(other_str)

    print("Content-Type: text/csv")
    print("Content-Disposition: attachment; filename=AeN_sample_database_export.csv\n")

    sys.stdout.flush()

    # Using sys, as print doesn't work for cgi in python3
    full_query = 'COPY (SELECT ' + get_fields(columns) + ',' + other_str + 'from aen where ' + filter_query +") TO STDOUT CSV HEADER"
    cur.copy_expert(full_query,sys.stdout.buffer)
   


    #with open(path, "rb") as f:
        #sys.stdout.flush()
        #shutil.copyfileobj(f, sys.stdout.buffer)

    cur.close()
    conn.close()
