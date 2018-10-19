--ACCESS=access content
select stationname, avg(decimallatitude) as avglat, avg(decimallongitude) as avglong ,avg(bottomdepthinmeters) as avgdepth from aen group by stationname order by stationname;
