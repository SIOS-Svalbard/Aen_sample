--ACCESS=access content
select eventdate, stationname, geartype, sampletype, eventID, parenteventID from aen
	where
    CASE when :startdate is not NULL THEN eventdate between :startdate AND  :enddate
    ELSE TRUE
    END
    AND
	CASE when :stationname is not NULL THEN stationname LIKE concat('%',:stationname,'%')
    ELSE TRUE
    END
    AND
    CASE when :geartype is not NULL THEN geartype LIKE concat('%',:geartype, '%') 
    ELSE TRUE
    END
    AND
    CASE when :sampletype is not NULL THEN sampletype LIKE concat('%',:sampletype,'%')
    ELSE TRUE
    END
    AND
    CASE when :cruisenumber is not NULL THEN cast(cruisenumber as text) LIKE :cruisenumber
    ELSE TRUE
    END
    AND
    CASE when :parenteventid is not NULL THEN cast(parenteventid as text) LIKE :parenteventid
    ELSE TRUE
    END
    AND
    CASE when :startlat is not NULL THEN decimallatitude between :startlat AND  :endlat
    ELSE TRUE
    END
    AND
    CASE when :startlon is not NULL THEN decimallongitude between :startlon AND  :endlon
    ELSE TRUE
    END
	order by eventdate, geartype, sampletype;
