from .person import Person

class Customer(Person):
    """
    Customer class inheriting from Person
    """
    def __init__(self, customer_id, name, mobile_number, address):
        super().__init__(customer_id, name, mobile_number, address)
        self.customer_id = customer_id
        self.purchase_history = []
    
    def buy_medicine(self, medicine, quantity, amount):
        """Record medicine purchase"""
        purchase = {
            'medicine_name': medicine.medicine_name,
            'quantity': quantity,
            'amount': amount,
            'timestamp': self._get_timestamp()
        }
        self.purchase_history.append(purchase)
        return purchase
    
    def view_purchase_history(self):
        """View customer purchase history"""
        return self.purchase_history
    
    def display_details(self):
        """Display customer details"""
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Mobile: {self.mobile_number}, Address: {self.address}, Purchases: {len(self.purchase_history)}"
    
    @staticmethod
    def _get_timestamp():
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def __str__(self):
        return f"Customer({self.customer_id}, {self.name})"
    
    def __repr__(self):
        return f"Customer(id={self.customer_id}, name={self.name}, purchases={len(self.purchase_history)})"
    
    def to_dict(self):
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'mobile_number': self.mobile_number,
            'address': self.address,
            'purchase_history': self.purchase_history
        }
