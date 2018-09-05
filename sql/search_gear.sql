--ACCESS=access content
select eventdate, stationname, geartype, sampletype, eventID, parenteventID from aen
	where lower(geartype) LIKE '%'||lower(:geartype)||'%'
	order by eventdate, geartype, sampletype;
