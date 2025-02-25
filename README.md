# BearerTokenExample
# BearerTokenExample

This project demonstrates how to interact with the Stripe API using a Bearer Token for authentication in Python. The example includes operations such as retrieving customers, creating a customer, getting a specific customer, and deleting a customer.

## Prerequisites

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```sh
pip install requests

Usage
Retrieve Customers  This section retrieves a list of customers from the Stripe API.  
response = requests.get(baseurl, headers=headers)
print(response.status_code)
print(response.json())
Create a Customer  This section creates a new customer with the provided email, name, and next invoice sequence.  
payload = "email=test2%40test.com&name=TestPython2&next_invoice_sequence=3"
response = requests.post(baseurl, headers=post_headers, data=payload)
print(response.status_code)
print(response.json()["id"])
new_customer_id = response.json()["id"]
Get a Customer  This section retrieves the details of a specific customer using their customer ID.  
customer_id = new_customer_id
response = requests.get(baseurl + "/" + customer_id, headers=headers)
print(response.status_code)
print(response.json())
Delete a Customer  This section deletes a specific customer using their customer ID.  
response = requests.delete(baseurl + "/" + customer_id, headers=headers)
print(response.status_code)
Delete a Non-Existing Customer  This section attempts to delete a non-existing customer and handles the case where the customer is not found.  
customer_id = "cus_RqDFQyyJ5sglwc"
response = requests.delete(baseurl + "/" + customer_id, headers=headers)
if response.status_code == 404:
    print("Customer not found")
Configuration
Replace the b_token variable with your actual Stripe API Bearer Token