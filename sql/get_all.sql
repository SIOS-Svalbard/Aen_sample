--ACCESS=access content
select * from aen
	order by eventdate, geartype, sampletype
    LIMIT :len OFFSET :offset ;
