from app.models.record import Record
from sqlalchemy import func,extract

def get_category_totals(db):
    result = (db.query(Record.category,Record.type,func.sum(Record.amount)).group_by(Record.category,Record.type).all())
    return[{"category":category,
           "type":type_,
           "total":total
    }for category,type_,total in result]



def get_summary(db):
    income = db.query(func.sum(Record.amount)).filter(Record.type == "income").scalar() or 0
    expense = db.query(func.sum(Record.amount).filter(Record.type =="expense")).scalar() or 0
    category_totals = get_category_totals(db)
    return { 
        "total_income":income,
        "total_expense":expense,
        "balance":income-expense,
        "category_totals":category_totals  }