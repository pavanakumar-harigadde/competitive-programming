# Write your MySQL query statement below
select name as Employee from Employee e 
    where e.salary > (select m.salary from Employee m where e.managerId=m.id )

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna