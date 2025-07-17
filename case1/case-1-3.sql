SELECT
    c.BUSINESS_NAME        AS business_area,
    SUM(s.SALES_VALUE)     AS total_sales_usd
FROM `looqbox-challenge`.data_store_sales AS s
JOIN `looqbox-challenge`.data_store_cad   AS c
      ON s.STORE_CODE = c.STORE_CODE
WHERE s.DATE >= '2019-01-01'
  AND s.DATE <  '2019-04-01'    
GROUP BY c.BUSINESS_NAME
ORDER BY total_sales_usd DESC;
