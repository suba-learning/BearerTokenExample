import requests

baseurl = "https://api.stripe.com/v1/customers"
b_token =  "sk_test_51QwVyg2f0hmox9OfPpe0TTGyiV2UkGh8VNRsYazCChr558b41FRfJuEljI7KZEpGp3r9stcKqgz4VkQJOO9g4qTZ00nj4XnVNW"

headers = {
    "Authorization": f"Bearer {b_token}",
    "Content-Type": "application/json"
}
#get customers
response = requests.get(baseurl, headers=headers)
print(response.status_code)
print(response.json())



#Create a customer
payload = "email=test2%40test.com&name=TestPython2&next_invoice_sequence=3"
post_headers={
    "Authorization": f"Bearer {b_token}",
    "Content-Type": "application/x-www-form-urlencoded",
}
response = requests.post(baseurl, headers=post_headers, data=payload)
print(response.status_code)
print(response.json()["id"])
new_customer_id = response.json()["id"]

#get a customer
customer_id = new_customer_id
response = requests.get(baseurl+"/"+customer_id , headers=headers)
print(response.status_code)
print(response.json())

#Delete a customer
print("Customer ID", customer_id)
response = requests.delete(baseurl+"/"+"customer_id" , headers=headers)
print(response.status_code)

#Delete non-existing customer
customer_id = "cus_RqDFQyyJ5sglwc"
response = requests.delete(baseurl+"/"+"customer_id" , headers=headers)
if (response.status_code)== 404:
    print("Customer not found")