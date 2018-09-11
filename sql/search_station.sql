--ACCESS=access content
select stationname, decimallatitude, decimallongitude from aen
	where stationname=:stationname AND
    sampletype = 'Station';
