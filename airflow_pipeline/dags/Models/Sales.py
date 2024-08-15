from dataclasses import dataclass
from datetime import datetime

@dataclass
class Sale:
    product_id: str
    store_id: str
    date: datetime
    sales: int
    revenue: float
    stock: int
    price: float
