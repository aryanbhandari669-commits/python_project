class Bill:
    """
    Bill class to manage billing
    """
    GST_RATE = (5, 12, 18)  # Different GST rates as tuple
    
    def __init__(self, bill_id, customer_name, medicines):
        self.bill_id = bill_id
        self.customer_name = customer_name
        self.medicines = medicines  # List of {medicine, quantity, price}
        self.total_amount = 0
        self.gst_amount = 0
        self.final_amount = 0
    
    def generate_bill(self, gst_rate=18):
        """Generate bill with GST calculation"""
        self.total_amount = sum(item['price'] * item['quantity'] for item in self.medicines)
        self.gst_amount = self.calculate_gst(gst_rate)
        self.final_amount = self.total_amount + self.gst_amount
        return True
    
    @staticmethod
    def calculate_gst(amount, gst_rate=18):
        """Calculate GST (static method)"""
        return (amount * gst_rate) / 100
    
    def print_bill(self):
        """Print bill details"""
        bill_str = f"\n{'='*50}\n"
        bill_str += f"BILL ID: {self.bill_id}\n"
        bill_str += f"Customer: {self.customer_name}\n"
        bill_str += f"{'-'*50}\n"
        bill_str += f"{'Medicine':<25} {'Qty':<8} {'Amount':<15}\n"
        bill_str += f"{'-'*50}\n"
        
        for item in self.medicines:
            amount = item['price'] * item['quantity']
            bill_str += f"{item['medicine']:<25} {item['quantity']:<8} {amount:<15.2f}\n"
        
        bill_str += f"{'-'*50}\n"
        bill_str += f"Subtotal: {self.total_amount:.2f}\n"
        bill_str += f"GST (18%): {self.gst_amount:.2f}\n"
        bill_str += f"Total: {self.final_amount:.2f}\n"
        bill_str += f"{'='*50}\n"
        
        return bill_str
    
    def __str__(self):
        return f"Bill({self.bill_id}, {self.customer_name})"
    
    def __repr__(self):
        return f"Bill(id={self.bill_id}, total={self.final_amount})"
    
    def to_dict(self):
        return {
            'bill_id': self.bill_id,
            'customer_name': self.customer_name,
            'medicines': self.medicines,
            'subtotal': self.total_amount,
            'gst': self.gst_amount,
            'total': self.final_amount
        }
