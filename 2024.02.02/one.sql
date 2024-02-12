-- 1
select avg(salary) from doctors;

select avg(premium) from doctors where salary > 72767.671429;

-- 2
select doctors_id, 
avg(datediff(end_date, start_date)) as days 
from vacations 
group by doctors_id order by days;

select doctors_id, 
min(year(start_date)) as 'start',
max(year(start_date)) as 'end' 
from vacations
group by doctors_id
order by 'start' - 'end'; 

-- 3
select departments_id, sum(amount) from donations 
group by departments_id
order by departments_id;

select sponsors_id, year(date) as time, sum(amount) from donations
group by sponsors_id, time
order by sponsors_id, time;
