use db_donations;
select * from tb_donations_points;

update tb_donations_points set point = replace(point, 'Ponto ', '');