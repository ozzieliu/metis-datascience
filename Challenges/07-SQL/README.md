# Challenge 7 - SQL

Topic: SQL Exercies
Date: 02/05/2016  
Name: Ozzie Liu

**Using the [Try SQL module on W3schools.com](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all),
answer the following questions:**

## 1. What customers are from the UK?

```sql
SELECT *
FROM Customers
WHERE Country="UK"
```

> Around the Horn
B's Beverages
Consolidated Holdings
Eastern Connection
Island Trading
North/South
Seven Seas Imports

## 2. What is the name of the customer who has the most orders?

```sql
SELECT CustomerName, COUNT(*)
FROM Orders
JOIN Customers
ON Orders.CustomerID=Customers.CustomerID
GROUP BY CustomerName
ORDER BY COUNT(*) DESC
LIMIT 1
```

> **Ernst Handel** with 10 orders

## 3. What supplier has the highest average product price?

```sql
SELECT SupplierName, AVG(Price)
FROM Suppliers
JOIN Products
ON Suppliers.SupplierID = Products.SupplierID
GROUP BY SupplierName
ORDER BY AVG(Price) DESC
LIMIT 1
```

> **Aux joyeux ecclésiastiques** with average of 140.75

## 4. How many different countries are there customers from? (Hint: Consider DISTINCT.)

```sql
SELECT COUNT(DISTINCT(Country))
FROM Customers
```

> **21** different countries

## 5. What category appears in the most orders?

```sql
SELECT CategoryName, SUM(Quantity) AS total
FROM OrderDetails
JOIN Products ON OrderDetails.ProductID=Products.ProductID
JOIN Categories ON Categories.CategoryID=Products.CategoryID
GROUP BY CategoryName
ORDER BY total DESC
/*LIMIT 1*/
```

> **Dairy Products** on 2601 orders


## 6. What was the total cost for each order?

```sql
SELECT Orders.OrderID as ID, SUM(Quantity*Price) as Total
FROM Orders
JOIN OrderDetails ON Orders.OrderID=OrderDetails.OrderID
JOIN Products ON OrderDetails.ProductID=Products.ProductID
GROUP BY ID
```

Here's a subset of the result:
> ID	Total
10248	566
10249	2329.25
10250	2267.25
10251	839.5
10252	4662.5

## 7. What employee made the most sales (by total cost)?

```sql
SELECT Employees.FirstName, SUM(Price*Quantity) as total
FROM Employees
JOIN Orders ON Employees.EmployeeID=Orders.EmployeeID
JOIN OrderDetails ON Orders.OrderID=OrderDetails.OrderID
JOIN Products ON OrderDetails.ProductID=Products.ProductID
GROUP BY Employees.FirstName
ORDER BY total DESC
```
> **Margaret** with 105696.49

## 8. What Employees have BS degrees? (Hint: Look at the LIKE operator.)

```sql
SELECT *
FROM Employees
WHERE Notes LIKE '%BS%'
```
> **Janet Leverling** and **Steven Buchanan**

## 9. What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)

```sql
SELECT SupplierName, COUNT(DISTINCT OrderDetails.ProductID) as num_products, AVG(Price) as avg_price
FROM OrderDetails
JOIN Products ON Products.ProductID=OrderDetails.ProductID
JOIN Suppliers ON Suppliers.SupplierID=Products.SupplierID
GROUP BY SupplierName
HAVING num_products >= 3
ORDER BY avg_price DESC
```

> **Plutzer Lebensmittelgroßmärkte AG** sells 5	products with average product price of 46.87
