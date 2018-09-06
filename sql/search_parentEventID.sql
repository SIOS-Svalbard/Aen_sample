--ACCESS=access content
select eventdate, stationname, geartype, sampletype, eventID, parenteventID from aen
	where parenteventID=:eventid
	order by eventdate, geartype, sampletype;
