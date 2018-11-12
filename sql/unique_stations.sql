--ACCESS=access content
select stationname, round(avg(decimallatitude)::numeric,4) as avglat, round(avg(decimallongitude)::numeric,4) as avglong , round(avg(bottomdepthinmeters)::numeric,1) as avgdepth, stationname as sname from aen group by stationname order by stationname;
