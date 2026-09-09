# Write your MySQL query statement below
Select  p.firstName, p.lastName, a.city , a.state 
from Person p LEFT JOIN Address a
ON p.personId=a.personId;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna