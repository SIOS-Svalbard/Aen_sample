--ACCESS=access content
select eventdate, stationname, geartype, sampletype, eventID, parenteventID from aen 
    where eventid in 
        (select cast(unnest(string_to_array(:eventids,' ')) as uuid)) 
	order by eventdate, geartype, sampletype;
