import pytest

from oop import oop

FILENAME = '../data.txt'

res = oop.read_file(FILENAME)


@pytest.mark.timeout(1.0)
def test_correct_invoices_amount():
    """Test has correct amount of invoices"""
    assert len(res) == 2


@pytest.mark.timeout(1.0)
def test_invoice_has_correct_rows_amount():
    """Test invoice has correct amount of rows"""
    for invoice in res:
        if invoice.invoice_no == '2':
            assert len(invoice.rows) == 2
            return
    else:
        assert False, 'Invoice 2 not found'


@pytest.mark.timeout(1.0)
def test_invoice_has_correct_product_qty():
    """Test invoice has correct product quantity"""
    for invoice in res:
        if invoice.invoice_no == '2':
            for row in invoice.rows:
                if row.product.product_name == 'Milk':
                    assert row.qty == 2
                    return
            else:
                assert False, 'Milk not found'
    else:
        assert False, 'Invoice 2 not found'


@pytest.mark.timeout(1.0)
def test_invoice_has_correct_product_total():
    """Test invoice has correct product total"""
    for invoice in res:
        if invoice.invoice_no == '2':
            for row in invoice.rows:
                if row.product.product_name == 'Milk':
                    assert row.total == 4.38
                    return
            else:
                assert False, 'Milk not found'
    else:
        assert False, 'Invoice 2 not found'
