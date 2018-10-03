--ACCESS=access content
select eventdate, stationname, bottomdepthinmeters, geartype, eventtime, decimallatitude, decimallongitude, eventID, other -> 'recordNumber' as recordnumber from aen
	where
    CASE when :startdate is not NULL THEN eventdate between :startdate AND  :enddate
    ELSE TRUE
    END
    AND
	CASE when :stationname is not NULL THEN stationname LIKE concat('%', :stationname ,'%')
    ELSE TRUE
    END
    AND
    CASE when :geartype is not NULL THEN geartype LIKE concat('%', :geartype , '%') 
    ELSE TRUE
    END
    AND
    CASE when :cruisenumber is not NULL THEN cast(cruisenumber as text) LIKE :cruisenumber
    ELSE TRUE
    END
    AND 
    parenteventid is NULL
	order by eventdate, eventtime;
