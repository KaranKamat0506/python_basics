from fastapi import FastAPI

#create an application
app = FastAPI()

#sample data
customers=[
    {"id":1, "name":"Harry", "city":"Mumbai"},
    {"id":2, "name":"Tom", "city":"Delhi"}
]
#Get api to fetch all customers
@app.get("/customers")
def get_customers():
    return customers

@app.get("/customers/{id}")
def get_customer(customer_id: int):
    for c in customers:
        if c["id"] == customer_id:
            return c
    return {"message": "customer not found"}

@app.post("/customers")
def add_customer(customer:dict):
    customers.append(customer)
    return {"message": "customer added successfully"}