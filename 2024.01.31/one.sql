-- 1
select name from country where continent = 'Europe' or continent = 'Asia';

select name, region from country where LifeExpectancy < 50;

select name, continent, surfacearea from country where continent = 'Africa' order by surfacearea desc limit 1;

select name from country where continent = 'Asia' order by (population / surfacearea) asc limit 5;


-- 2
select countrycode, name from city where population > 5000000 order by population desc;

select countrycode, name from city where countrycode = 'IND' order by char_length(name) desc limit 1;