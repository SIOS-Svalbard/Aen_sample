--ACCESS=access content
select eventdate, stationname, geartype, sampletype, eventID, parenteventID from aen
	order by eventdate, geartype, sampletype;
