from .person import Person

class Supplier(Person):
    """
    Supplier class inheriting from Person
    """
    def __init__(self, supplier_id, name, mobile_number, address):
        super().__init__(supplier_id, name, mobile_number, address)
        self.supplier_id = supplier_id
        self.supplied_medicines = []
    
    def supply_medicine(self, medicine_name, quantity, price, date):
        """Record medicine supply"""
        supply_record = {
            'medicine_name': medicine_name,
            'quantity': quantity,
            'price': price,
            'supply_date': date
        }
        self.supplied_medicines.append(supply_record)
        return supply_record
    
    def view_supply_details(self):
        """View supplier supply details"""
        return self.supplied_medicines
    
    def display_details(self):
        """Display supplier details"""
        return f"Supplier ID: {self.supplier_id}, Name: {self.name}, Mobile: {self.mobile_number}, Address: {self.address}, Medicines Supplied: {len(self.supplied_medicines)}"
    
    def __str__(self):
        return f"Supplier({self.supplier_id}, {self.name})"
    
    def __repr__(self):
        return f"Supplier(id={self.supplier_id}, name={self.name}, supplies={len(self.supplied_medicines)})"
    
    def to_dict(self):
        return {
            'supplier_id': self.supplier_id,
            'name': self.name,
            'mobile_number': self.mobile_number,
            'address': self.address,
            'supplied_medicines': self.supplied_medicines
        }
