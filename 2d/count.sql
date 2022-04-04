select  E.FirstName || ' ' || E.LastName as name, count(Total) as s
from Invoice
join Customer c on c.CustomerId=Invoice.CustomerId
join Employee E on C.SupportRepId = E.EmployeeId
where CAST(SUBSTR(invoiceDate, 1, 4) AS integer) >= 2010
group by EmployeeId
order by s desc
limit 3
