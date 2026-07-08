from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Classified Ads API",
    description="API для доски объявлений (как Avito)",
    version="1.0.0"
)


@app.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


@app.get("/categories/", response_model=List[schemas.Category])
def get_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/ads/", response_model=schemas.Ad)
def create_ad(ad: schemas.AdCreate, db: Session = Depends(get_db)):
    db_ad = models.Ad(**ad.dict(), author_id=1)
    db.add(db_ad)
    db.commit()
    db.refresh(db_ad)
    return db_ad


@app.get("/ads/", response_model=List[schemas.Ad])
def get_ads(
        category_id: int = None,
        min_price: int = None,
        max_price: int = None,
        location: str = None,
        db: Session = Depends(get_db)
):
    query = db.query(models.Ad).filter(models.Ad.is_active == True)

    if category_id:
        query = query.filter(models.Ad.category_id == category_id)
    if min_price:
        query = query.filter(models.Ad.price >= min_price)
    if max_price:
        query = query.filter(models.Ad.price <= max_price)
    if location:
        query = query.filter(models.Ad.location.ilike(f"%{location}%"))

    return query.all()


@app.get("/ads/{ad_id}", response_model=schemas.Ad)
def get_ad(ad_id: int, db: Session = Depends(get_db)):
    ad = db.query(models.Ad).filter(models.Ad.id == ad_id).first()
    if not ad:
        raise HTTPException(status_code=404, detail="Ad not found")
    return ad


@app.put("/ads/{ad_id}", response_model=schemas.Ad)
def update_ad(ad_id: int, ad_update: schemas.AdUpdate, db: Session = Depends(get_db)):
    db_ad = db.query(models.Ad).filter(models.Ad.id == ad_id).first()
    if not db_ad:
        raise HTTPException(status_code=404, detail="Ad not found")

    for key, value in ad_update.dict(exclude_unset=True).items():
        setattr(db_ad, key, value)

    db.commit()
    db.refresh(db_ad)
    return db_ad


@app.delete("/ads/{ad_id}")
def delete_ad(ad_id: int, db: Session = Depends(get_db)):
    db_ad = db.query(models.Ad).filter(models.Ad.id == ad_id).first()
    if not db_ad:
        raise HTTPException(status_code=404, detail="Ad not found")

    db_ad.is_active = False
    db.commit()
    return {"message": "Ad deactivated successfully"}


@app.get("/")
def root():
    return {
        "message": "Classified Ads API",
        "docs": "/docs",
        "version": "1.0.0"
    }
