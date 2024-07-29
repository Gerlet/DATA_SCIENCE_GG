select count(*) from empleado;
select max(salario),min(salario),avg(salario) from empleado;

select distinct area from empleado;

select area,max(salario),min(salario),avg(salario)
from empleado
group by area
order by max(salario) desc

select * from empleado
where salario > (select avg(salario) from empleado);
