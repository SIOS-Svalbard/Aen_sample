--ACCESS=access content
select eventdate, stationname, geartype, sampletype, eventID, parenteventID from aen
	where eventdate between :startdate AND  :enddate AND
	stationname LIKE :stationname AND 
	geartype LIKE :geartype AND 
	sampletype LIKE :sampletype AND
       	cast(cruisenumber as text) LIKE :cruisenumber AND 
	cast(parenteventID as text) LIKE :parenteventid
	order by eventdate, geartype, sampletype;
