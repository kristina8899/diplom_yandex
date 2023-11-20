1. SELECT login, Count ("inDelivery") FROM "Orders" JOIN "Couriers" ON "Couriers"."id" = "Orders"."id"  WHERE "inDelivery" = true GROUP BY "Couriers"."login"; 

2. SELECT track, CASE 
WHEN "inDelivery" = true THEN 1 
WHEN "cancelled" = true THEN -1 
WHEN "finished" = true THEN 2 ELSE 0 
END AS update_order 
FROM "Orders";