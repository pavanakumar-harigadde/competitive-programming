# Write your MySQL query statement below
select * from Cinema c 
    where (c.id % 2)!=0 
    and c.description !="boring"
    ORDER BY rating DESC

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna