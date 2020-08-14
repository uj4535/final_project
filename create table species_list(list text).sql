create table species_list(list text)







-- select species from animal_list group by species having count(*) <40
-- delete from animal_list where  species IN (select * from (select species from animal_list group by species having count(*) <40))