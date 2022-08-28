CREATE TABLE hex_grace AS
SELECT hex,
count(*),
count(case when label=0 then 1 end) as count0,
count(case when label=1 then 1 end) as count1,
count(case when label=0 then 1 end)::numeric/count(*) as count0p,
count(case when label=1 then 1 end)::numeric/count(*) as count1p
--label, period, subject_type, subject_name, city_name, hex, hex_lat, hex_lon, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30
	FROM public.train_ds_clean
	group by hex
	
select tr.*, h.*
from train_ds_final tr
left join hex_grace h on tr.hex = h.hex

