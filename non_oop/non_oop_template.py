"""MX - Structuring data: OOP vs non-OOP."""


def is_product_in_invoice(product_name: str, invoice: list[list]) -> bool:
    """
    Checks that the invoice has a product with the given name.

    Args:
        product_name: The name of the product.
        invoice: The list that contains the product name.

    Returns:
        bool: True or false.
    """
    pass


def calculate_total(unit_price: float, qty: float) -> float:
    """
    Calculates the total revenue gained from the product.

    Return:
        float: The total rounded to 2 decimal places.
    """
    pass


def update_product_qty(invoice: list[list], product_name: str, qty: float):
    """
    Updates the product's quantity if the product is already present.

    Args:
        invoice: The list that contains the product name and its quantity.
        product_name: The name of the product.
        qty: The quantity for the product.
    """
    pass


def read_file(filename: str) -> dict[str, list[list]]:
    """
    Reads the file into a dictionary of invoices.

    Each line has the following columns: invoice number, product name, unit price and quantity.

    Example:
    1,Banana,1.59,0.69

    Should become:
    {'1': [['Banana', 1.59, 0.69, 1.1]]}

    Each invoice row has the product name, unit price, quantity and total.

    If an invoice has multiple products with the same name, then add those together.

    Instead of:
    {'1': [
        ['Banana', 1.59, 0.69, 1.1],
        ['Banana', 1.59, 0.69, 1.1]
    ]}

    Should become:
    {'1': [['Banana', 1.59, 1.38, 2.19]]}

    Args:
        filename: The name of the file.

    Returns:
        list: A dictionary of invoices.
    """
    pass


if __name__ == '__main__':
    print(read_file('../data.txt'))
