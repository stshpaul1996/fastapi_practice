from fastapi import FastAPI,status,Depends, HTTPException, Response
from sqlalchemy.orm import Session 
import uvicorn
from typing import List

import schemas
from database import get_db
import models


app = FastAPI()


@app.post("/product", status_code=status.HTTP_201_CREATED, response_model=schemas.ProductOut)
def product(request: schemas.ProductIn, db:Session=Depends(get_db)):
    data = request.dict()
    post = models.Product(**data)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


@app.get("/product", response_model=List[schemas.ProductOut])
def product(db:Session=Depends(get_db)):
    query = db.query(models.Product).all()
    return query


@app.get("/product/{id}", response_model=schemas.ProductOut)
def product(id:int, db:Session=Depends(get_db)):
    get = db.query(models.Product).filter(models.Product.id == id).first()
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"product with id:{id} does not exists")
    return get

@app.put("/product/{id}")
def product(id:int, request:schemas.ProductIn, db:Session=Depends(get_db)):
    get = db.query(models.Product).filter(models.Product.id==id).first()
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'product with id:{id} does not exists')
    
    for key, value in request.dict().items():
        setattr(get, key, value)
 
    db.commit()
    return {"detail":f"with id:{id} updated successuflly"}

@app.delete("/product/{id}")
def product(id:int, db:schemas=Depends(get_db)):
    get = db.query(models.Product).filter(models.Product.id == id).first()
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'product with id:{id} not found')
    db.delete(get)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT, detail=f"deleted successfully with id:{id}")

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)