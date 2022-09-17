from fastapi import FastAPI
import order, product

app = FastAPI()

#including routers
app.include_router(product.router)
app.include_router(order.router)

#default
@app.get("/")
def welcome_page():
    return {"message": "Welcome to bepragma:)"}
    
