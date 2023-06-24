# Structuring data: OOP vs non-OOP

## Background

You are an IT specialist in a local shop. The store keeps every invoice ever created in one file, and it sucks.
The invoices are unsorted, some data is duplicated, and they're not human-readable.
Your job to make sense of these invoices and gather them into a coherent form.

## Task description

There is a file where each line represents a row in an invoice. Read the file and put the rows under the correct invoice.
Each line has the following columns: invoice number, product name, unit price and quantity.

### Requirements

* If an invoice has multiple products with the same name, then add those together.