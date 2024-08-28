import pandas as pd


def calculate_sales_stats(sales_data_file: str) -> tuple:
    """Calculates stats such as total sales, average sales
       and number of entries in the given 'sales_data_file'.

    Args:
        sales_data_file: Full path to the sales data file.

    Returns:
        A tuple total_sales, average_sales, total_sales.
    """
    data_frame = pd.read_csv(sales_data_file)
    total_sales = data_frame["Sales"].sum()
    average_sales = data_frame["sales"].mean()
    number_of_entries = total_sales // average_sales
    return total_sales, average_sales, number_of_entries


if __name__ == "__main__":
    total_sales, average_sales, number_of_entries = calculate_sales_stats(
        "groceries_sales_data.csv"
    )
    print("Total Sales: ", round(total_sales, 2)) # 15466529.6
    print("Average Sales: ", round(average_sales, 2))# 20458.37
    print("Number of Entries: ", number_of_entries) # 756
