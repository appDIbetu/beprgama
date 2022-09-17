#script to do crud operation of order

from fastapi import APIRouter
import model
from sqlmodel import Session, create_engine, select

#router
router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

#sqlite db details
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

#API works starts here

#API to create orders
#SQLModels as the parameters as they act as both pydantic and SQLAlchemy data models

#we can use "Body" as well instead of parameter by importing it from FastAPI but for swagger UI
#the arguments method itself is used.
@router.post("/")
def createOrder(order:model.Order, customer:model.Customer, productList:model.ProductList):
    

    #with attribute for closing the session at ease in case of errors as well to run block and end up the session
    with Session(engine) as session:

        #assume products have already been created 
        #if customer id is there use that else 
        #create a new customer with the help of SQLModel relationship attributes

        #create a order with the help of SQLModel relationship attributes in order_items
        #this is going to prevent us creating separate order instance and comitting again and again

        #relationship attribute will handle data sharing with all other instances(so called data tables) at ease.
        #product = model.Product(price=10.0, name="Apple")

        #iterate through all order_items received in payload arguments
        for orderItem in productList.data:
            if(customer.id):
                orderItem.customer_id = customer.id
                order.customer_id = customer.id
            else:
                orderItem.customer = customer
                order.customer = customer
            
            orderItem.order = order
            session.add(orderItem)
            
        session.commit()
        session.close()

    return {"message": "order created successfully:)"}



#API to get order details by order_id as path parameter
@router.get("/{order_id}")
def read_order_by_id(order_id:int):
    with Session(engine) as session:
        statement = select(model.Order).where(model.Order.id == order_id)
        result = session.exec(statement)
        #checking if a row exists and send data if exists else none
        order = result.first()
        if(order):
            customer = order.customer
            order_items = order.order_items
            session.close()
            response = {"message": "Data fetched Successfully:)",
                    "data": {
                        "order_info": order,
                        "customer": customer,
                        "order_items": order_items}}
        else:
            session.close()
            response = {"message": "No data found:(", "data": None}

    return response



#API to fetch all orders and its corresponding details
@router.get("/")
def read_all_orders():
    with Session(engine) as session:
        statement = select(model.Order)
        orders = session.exec(statement)
        #checking if a row exists and send data if exists else none
        #order = results.first()
        #if(results):
        orderList = []
        for order in orders:
            customer = order.customer
            order_items = order.order_items
            orderList.append({
                    "order_info": order,
                    "customer": customer,
                    "order_items": order_items})


        if (orderList):
            session.close()
            response = {"message": "Data fetched Successfully:)", "data": orderList}
        else:
            session.close()
            response = {"message": "No data found:(", "data": None}

    return response



#API to delete order details by order_id as path parameter
@router.delete("/{order_id}")
def delete_order_by_id(order_id:int):
    with Session(engine) as session:
        statement = select(model.Order).where(model.Order.id == order_id)
        result = session.exec(statement)
        order = result.first()

        if(order):
            session.delete(order)
            session.commit()
            session.close()
            response = {"message": "Data deleted successfully:)", "data": order}
        else:
            session.close()
            response = {"message": "No data found to be deleted:(", "data": None}
        
        return response



#API to update order details by order_id as path parameter
#we can update whole object by reading the corresponding data through user Interface
#by passing the argument parameters which has been fetched as we do in create orders

#alternatively we can update basic attributes like amount, customer_id and 
#major updates like add product in order by appending new order_item 
#or completely replacing customer instance as fas we keep unique order id consistent

#or we can put all details consistent(constant) and vary order id itself, that will require 
# deleting old one and creating new one in same call

#a basic update API with comments is shown below
@router.put("/{order_id}")
def delete_order_by_id(order_id:int, amount: float, updated_order:model.Order
, new_product_list:model.ProductList, single_order_item:model.OrderItem, updated_customer: model.Customer):
    with Session(engine) as session:
        statement = select(model.Order).where(model.Order.id == order_id)
        result = session.exec(statement)
        order = result.first()

        if(order):
            #update basic infos:
            if(amount):
                order.amount = updated_order.amount

            #append new product
            if(single_order_item):
                order.order_items.append(single_order_item)

            #and many other flows... 
            session.add(order)
            session.commit()
            session.close()
            response = {"message": "Order updated successfully:)", "data": order}
        else:
            session.close()
            response = {"message": "No order with given order id found to be updated:(", "data": None}
        
        return response