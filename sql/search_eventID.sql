--ACCESS=access content
/*CREATE OR REPLACE FUNCTION json_to_html(s text) RETURNS text
	AS $$
	BEGIN
	  s := replace(s,'{"','<div><table><tbody><tr><th>');
	  s := replace(s,'"}','</tbody></th></tr></table></div>');
	  s := replace(s,'": "','<tr><th>');
	  s := replace(s,'", "','</td></tr></tbody><tbody><tr><th>');
	  RETURN s;
	END;
	$$ LANGUAGE plpgsql stable;*/

select *, replace(replace(replace(replace(replace(cast(hstore_to_json(other) as text),'{"','<div><table><tbody><tr><th>'),'"}' ,'</tbody></th></tr></table></div>'),'": "','</th><td>'),'", "','</td></tr></tbody><tbody><tr><th>'),'_',' ') as other_form ,  
replace(replace(replace(replace(replace(cast(hstore_to_json(metadata) as text),'{"','<div><table><tbody><tr><th>'),'"}','</tbody></th></tr></table></div>'),'": "','</th><td>'),'", "','</td></tr></tbody><tbody><tr><th>'),'_',' ') as metadata_form from aen
	where eventid=:eventid
        order by eventdate, geartype, sampletype;                             
