--ACCESS=access content
select eventdate, stationname, geartype, sampletype, eventID, parenteventID from aen
	where eventdate between :startdate AND  :enddate AND
	CASE when :stationname is not NULL THEN stationname LIKE :stationname
    ELSE TRUE
    END
    AND
    CASE when :geartype is not NULL THEN geartype LIKE :geartype 
    ELSE TRUE
    END
    AND
    CASE when :sampletype is not NULL THEN sampletype LIKE :sampletype
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
	order by eventdate, geartype, sampletype;
