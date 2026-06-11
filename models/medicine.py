from datetime import datetime

class Medicine:
    """
    Medicine class to manage medicine details
    """
    def __init__(self, medicine_id, medicine_name, company_name, category, price, quantity, expiry_date):
        self.medicine_id = medicine_id
        self.medicine_name = medicine_name
        self.company_name = company_name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.expiry_date = expiry_date
    
    def add_medicine(self, quantity):
        """Add medicine to stock"""
        self.quantity += quantity
        return self.quantity
    
    def update_stock(self, quantity):
        """Update medicine stock"""
        if quantity <= self.quantity:
            self.quantity -= quantity
            return True
        return False
    
    def check_expiry(self):
        """Check if medicine is expired"""
        expiry_date = datetime.strptime(self.expiry_date, "%Y-%m-%d")
        current_date = datetime.now()
        return expiry_date < current_date
    
    def display_medicine(self):
        """Display medicine details"""
        return f"ID: {self.medicine_id}, Name: {self.medicine_name}, Company: {self.company_name}, Category: {self.category}, Price: {self.price}, Qty: {self.quantity}, Expiry: {self.expiry_date}"
    
    def __str__(self):
        return f"{self.medicine_name} ({self.medicine_id})"
    
    def __repr__(self):
        return f"Medicine(id={self.medicine_id}, name={self.medicine_name}, qty={self.quantity})"
    
    def to_dict(self):
        return {
            'medicine_id': self.medicine_id,
            'medicine_name': self.medicine_name,
            'company_name': self.company_name,
            'category': self.category,
            'price': self.price,
            'quantity': self.quantity,
            'expiry_date': self.expiry_date,
            'is_expired': self.check_expiry()
        }
