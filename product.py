#script to create product

from fastapi import APIRouter
import model
from sqlmodel import Session, create_engine

#router
router = APIRouter(
    prefix="/products",
    tags=["products"]
)

#sqlite db details
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)


#API works starts here
@router.post("/")
def createProduct(product:model.Product):
    
    with Session(engine) as session:

        session.add(product)
        session.commit()
        session.close()

    return {"message": "Product added successfully."}