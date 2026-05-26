import sqlite3
import pandas as pd

def ask_database(question):
    conn = sqlite3.connect("store.db")

    question = question.lower()

    if "total sales" in question:
        sql = """
        SELECT SUM(SALES) AS Total_Sales
        FROM sales
        """

    elif "technology sales" in question:

        sql = """
        SELECT SUM(Sales) AS Technology_Sales
        FROM Sales
        """

    elif "profit" in question:

        sql = """
        SELECT SUM(Sales) AS Total_Profit
        FROM Sales
        """

    elif "furniture sales" in question:

        sql = """
        SELECT SUM(Sales) AS Furniture_Sales
        FROM Sales
        """

    elif "office sales" in question:

        sql = """
        SELECT SUM(Sales) AS Office_Sales
        FROM Sales
        """

    elif "top 5 products" in question:

        sql = """
       SELECT [Product Name], Sales
       from sales
       order by Sales desc
       limit 5
        """

    elif "top 10 customers" in question:

        sql = """
      SELECT [Customer Name],
      sum(Sales) as Total
      from sales
      group by [Customer Name]
      order by Total desc
      limit 10
        """

    elif "average sales" in question:

        sql = """
      SELECT AVG(Sales)
      as Average_Sales
      from sales
        """

    elif "highest profit" in question:

        sql = """
       SELECT max(Profit)
       as Highest_Profit
       from sales
        """

    elif "total orders" in question:

        sql = """
       SELECT count(*)
       as Total_Orders
       from sales
        """

    elif "sales by region" in question:

        sql = """
       SELECT Region,
       sum(Sales) as Total_Sales
       from sales
       group by Region
        """

    elif "sales by state" in question:

        sql = """
       SELECT [State/Province],
       sum(Sales) as total_Sales
       from sales
       group by [State/Province]
       order by Total_Sales desc
       limit 10
        """

    else:
        conn.close()
        return "Question not supported."

    result = pd.read_sql(sql, conn)

    conn.close()

    return result