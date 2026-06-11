from datetime import datetime

class Sale:
    """
    Sale class to manage medicine sales
    """
    def __init__(self, sale_id, customer, medicine, quantity, sale_date=None):
        self.sale_id = sale_id
        self.customer = customer
        self.medicine = medicine
        self.quantity = quantity
        self.sale_date = sale_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def process_sale(self):
        """Process the sale"""
        if self.medicine.check_expiry():
            raise Exception(f"Medicine {self.medicine.medicine_name} is expired")
        
        if self.medicine.quantity < self.quantity:
            raise Exception(f"Insufficient stock for {self.medicine.medicine_name}")
        
        self.medicine.update_stock(self.quantity)
        return True
    
    def calculate_total(self):
        """Calculate total sale amount"""
        return self.medicine.price * self.quantity
    
    def __str__(self):
        return f"Sale({self.sale_id}, {self.customer.name}, {self.medicine.medicine_name})"
    
    def __repr__(self):
        return f"Sale(id={self.sale_id}, qty={self.quantity}, total={self.calculate_total()})"
    
    def to_dict(self):
        return {
            'sale_id': self.sale_id,
            'customer_name': self.customer.name,
            'medicine_name': self.medicine.medicine_name,
            'quantity': self.quantity,
            'unit_price': self.medicine.price,
            'total_amount': self.calculate_total(),
            'sale_date': self.sale_date
        }
