import requests
response = requests.get("http://localhost:8000/expenses/2024-08-08")
print(response.json())
print(len(response.json()))
print()
response2 = requests.get("http://localhost:8000/expenses/2024-08-07")
print(response2.json())
print(len(response2.json()))
print()
print()


if 'message' in response2.json():
    print("No expenses found for this date.")
if 'message' in response.json():
    print("No expenses found for this date.")