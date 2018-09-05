--ACCESS=access content
select eventdate, stationname, geartype, sampletype, eventID, parenteventID from aen
	where lower(sampletype) LIKE '%'||lower(:sampletype)||'%'
	order by eventdate, geartype, sampletype;
