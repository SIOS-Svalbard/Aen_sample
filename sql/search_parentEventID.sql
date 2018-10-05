--ACCESS=access content
select eventdate, stationname, geartype, sampletype, eventID, parenteventID, other -> 'recordNumber' as recordnumber from aen
	where parenteventID=:eventid
	order by eventdate, geartype, sampletype;
