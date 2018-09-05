--ACCESS=access content
select eventdate, stationname, geartype, sampletype, eventID, parenteventID from aen
	where stationname=:stationname
	order by eventdate, geartype, sampletype;
