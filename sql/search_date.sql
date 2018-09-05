--ACCESS=access content
select eventdate, stationname, geartype, sampletype, eventID, parenteventID from aen
	where eventdate=:eventdate
	order by eventdate, geartype, sampletype;
