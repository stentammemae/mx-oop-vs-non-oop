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
    return any(row[0] == product_name for row in invoice)


def calculate_total(unit_price: float, qty: float) -> float:
    """
    Calculates the total revenue gained from the product.

    Return:
        float: The total rounded to 2 decimal places.
    """
    return round(unit_price * qty, 2)


def update_product_qty(invoice: list[list], product_name: str, qty: float):
    """
    Updates the product's quantity if the product is already present.

    Args:
        invoice: The list that contains the product name and its quantity.
        product_name: The name of the product.
        qty: The quantity for the product.
    """
    for row in invoice:
        if row[0] == product_name:
            row[2] += qty
            row[3] = calculate_total(row[1], row[2])
            break


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
    with open(filename) as file:
        contents = file.read()
        content_list = contents.split('\n')
        res = {}
        for item in content_list:
            data = item.split(',')

            invoice_no = data[0]
            product_name = data[1]
            unit_price = float(data[2])
            qty = float(data[3])

            if invoice_no in res and is_product_in_invoice(product_name, res[invoice_no]):
                update_product_qty(res[invoice_no], product_name, qty)
            elif invoice_no in res and not is_product_in_invoice(product_name, res[invoice_no]):
                res[invoice_no].append([product_name, unit_price, qty, calculate_total(unit_price, qty)])
            elif invoice_no not in res:
                res[invoice_no] = [[product_name, unit_price, qty, calculate_total(unit_price, qty)]]
    return res


if __name__ == '__main__':
    print(read_file('../data.txt'))
