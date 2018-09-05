--ACCESS=access content
select eventdate, stationname, geartype, sampletype, eventID, parenteventID from aen
	where cruisenumber=:cruisenumber
	order by eventdate, geartype, sampletype;
