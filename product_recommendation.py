#script to recommend product based on product_id

from fastapi import APIRouter
import model
from sqlmodel import Session, create_engine, select

#router
router = APIRouter(
    prefix="/recommender",
    tags=["orders"]
)

#sqlite db details
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

#API to get products recomendation by product_id as path parameter
@router.get("/{product_id}")
def read_order_by_id(product_id:int):
    with Session(engine) as session:
        statement = select(model.Product).where(model.Product.id == product_id)
        result = session.exec(statement)
        #checking if a row exists and send data if exists else none
        product = result.first()

        if(product):
            #getting list of products
            statement = select(model.Product).where(model.Product.category == product.category)
            results = session.exec(statement)
            products = results.all()

            #sort products with maximum sales
            products.sort(key=lambda x: len(x.order_items), reverse=True)
            response = {"message": "Recommended Products",
                   "data": products}
        else:
            session.close()
            response = {"message": "No data found:(", "data": None}
        

    return response