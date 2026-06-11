class Inventory:
    """
    Inventory class to manage medicine inventory
    """
    def __init__(self, inventory_id):
        self.inventory_id = inventory_id
        self.medicine_list = {}
    
    def add_stock(self, medicine):
        """Add medicine to inventory"""
        self.medicine_list[medicine.medicine_id] = medicine
        return True
    
    def remove_stock(self, medicine_id, quantity):
        """Remove medicine from inventory"""
        if medicine_id in self.medicine_list:
            medicine = self.medicine_list[medicine_id]
            if medicine.quantity >= quantity:
                medicine.quantity -= quantity
                return True
        return False
    
    def check_low_stock(self, threshold=10):
        """Check for low stock medicines"""
        low_stock_medicines = []
        for medicine in self.medicine_list.values():
            if medicine.quantity < threshold:
                low_stock_medicines.append(medicine)
        return low_stock_medicines
    
    def view_inventory(self):
        """View all medicines in inventory"""
        return list(self.medicine_list.values())
    
    def get_medicine(self, medicine_id):
        """Get specific medicine from inventory"""
        return self.medicine_list.get(medicine_id)
    
    def update_medicine(self, medicine_id, **kwargs):
        """Update medicine details"""
        if medicine_id in self.medicine_list:
            medicine = self.medicine_list[medicine_id]
            for key, value in kwargs.items():
                if hasattr(medicine, key):
                    setattr(medicine, key, value)
            return True
        return False
    
    def __repr__(self):
        return f"Inventory(id={self.inventory_id}, medicines={len(self.medicine_list)})"
