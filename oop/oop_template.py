"""MX - Structuring data: OOP vs non-OOP."""


class Product:
    """Product class."""

    def __init__(self, product_name: str, unit_price: float):
        """
        Initializes a new Product with the given attributes.

        Args:
            product_name: The name of product.
            unit_price: The price for one unit of product.
        """
        self.product_name = product_name
        self.unit_price = unit_price

    def __repr__(self):
        """
        Returns a string representation of the Product instance.

        Returns:
            str: A string describing the product's name and unit price.
        """
        return f'Product({self.product_name}, {self.unit_price})'

    def __eq__(self, other):
        """
        Compares the product's name and unit price.

        Args:
            other: The object to compare with.

        Returns:
            bool: True or false.
        """
        return isinstance(other, Product) \
            and self.product_name == other.product_name \
            and self.unit_price == other.unit_price


class Row:
    """Row class."""

    def __init__(self, product: Product, qty: float):
        """
        Initializes a new Row with the given attributes.

        Args:
            product: The instance of Product.
            qty: The quantity of products.
        """
        self.product = product
        self.qty = qty
        self.total = 0
        self.set_total()

    def set_total(self):
        """
        Sets the total revenue gained from the product.

        Total must be rounded to 2 decimal places.
        """
        pass

    def increase_qty_by(self, qty: float):
        """
        Increases quantity by the amount specified and recalculates the total.

        Args:
            qty: The quantity for the product.
        """
        pass

    def __repr__(self):
        """
        Returns a string representation of the Row instance.

        Returns:
            str: A string describing the row's product, quantity and total.
        """
        return f'Row({self.product}, {self.qty}, {self.total})'


class Invoice:
    """Invoice class."""

    def __init__(self, invoice_no: str):
        """
        Initializes a new Invoice with the given attribute.

        Args:
            invoice_no: The identifying number for the invoice.
        """
        self.invoice_no = invoice_no
        self.rows: list[Row] = []

    def add_row(self, row: Row):
        """
        Adds a row to the invoice.

        Args:
            row: The instance of Row.
        """
        pass

    def update_product_qty(self, product: Product, qty: float):
        """
        Updates the product's quantity if the product is already present. Otherwise, it adds a new row for the product.

        Args:
            product: The instance of Product.
            qty: The quantity for the product.
        """
        pass

    def __repr__(self):
        """
        Returns a string representation of the Invoice instance.

        Returns:
            str: A string describing the invoice's number and rows.
        """
        res = f'Invoice({self.invoice_no}'

        for row in self.rows:
            res += ', ' + str(row)

        return res + ')'


def read_file(filename: str) -> list[Invoice]:
    """
    Reads the file into a list of invoices.

    Each line has the following columns: invoice number, product name, unit price and quantity.

    Example:
    1,Banana,1.59,0.69

    Should become:
    [Invoice(1, Row(Product(Banana, 1.59), 0.69, 1.1))]

    Each invoice row has the product, its quantity and total.

    If an invoice has multiple products with the same name, then add those together.

    Instead of:
    [Invoice(1,
        Row(Product(Banana, 1.59), 0.69, 1.1),
        Row(Product(Banana, 1.59), 0.69, 1.1))
    ]

    Should become:
    [Invoice(1, Row(Product(Banana, 1.59), 1.38, 2.19))]

    Args:
        filename: The name of the file.

    Returns:
        list: A list of invoices.
    """
    pass


if __name__ == '__main__':
    print(read_file('../data.txt'))
