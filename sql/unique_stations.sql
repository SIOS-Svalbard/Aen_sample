--ACCESS=access content
select uniqueStation, round(avg(decimallatitude)::numeric,4) as avglat, round(avg(decimallongitude)::numeric,4) as avglong , round(avg(bottomdepthinmeters)::numeric,1) as avgdepth, uniqueStation as sname from aen group by uniqueStation order by uniqueStation;
