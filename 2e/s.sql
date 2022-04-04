--решение неверное
select Track.trackid, count(Invoice.Invoiceid) as s
from Invoice, InvoiceLine, Track
where CAST(SUBSTR(invoiceDate, 1, 4) AS integer) >= 2010
group by Track.trackid
order by Track.trackid, s desc