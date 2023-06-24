import pytest

from non_oop import non_oop

FILENAME = '../data.txt'

res = non_oop.read_file(FILENAME)


@pytest.mark.timeout(1.0)
def test_correct_invoices_amount():
    """Test has correct amount of invoices"""
    assert len(res) == 2


@pytest.mark.timeout(1.0)
def test_invoice_has_correct_rows_amount():
    """Test invoice has correct amount of rows"""
    if '2' in res:
        assert len(res['2']) == 2
    else:
        assert False, 'Invoice 2 not found'


@pytest.mark.timeout(1.0)
def test_invoice_has_correct_product_qty():
    """Test invoice has correct product quantity"""
    if '2' in res:
        for row in res['2']:
            if row[0] == 'Milk':
                assert row[2] == 2
                return
        else:
            assert False, 'Milk not found'
    else:
        assert False, 'Invoice 2 not found'


@pytest.mark.timeout(1.0)
def test_invoice_has_correct_product_total():
    """Test invoice has correct product total"""
    if '2' in res:
        for row in res['2']:
            if row[0] == 'Milk':
                assert row[3] == 4.38
                return
        else:
            assert False, 'Milk not found'
    else:
        assert False, 'Invoice 2 not found'
