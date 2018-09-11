--ACCESS=access content
Select  CASE
	WHEN EXISTS(select stationname from aen where stationname = :stationname AND sampletype = 'Station')
	THEN 'a defined position'
	ELSE 'an average over its gear casts'
	END as info,

	COALESCE(
		(select stationname from aen where stationname = :stationname AND sampletype = 'Station' ),
		(select stationname from aen where stationname = :stationname LIMIT 1)
		) as stationname,

	COALESCE(
		(select decimallatitude from aen where stationname = :stationname AND sampletype = 'Station'),
		(select avg(decimallatitude) as avglat from aen where stationname = :stationname)
		) as decimallatitude,

	COALESCE(
		(select decimallongitude from aen where stationname = :stationname AND sampletype = 'Station'),
		(select avg(decimallongitude) as avglong from aen where stationname = :stationname)
		) as decimallongitude;
