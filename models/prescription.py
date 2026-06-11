class Prescription:
    """
    Prescription class to manage prescriptions
    """
    def __init__(self, prescription_id, doctor_name, patient_name, prescribed_medicines):
        self.prescription_id = prescription_id
        self.doctor_name = doctor_name
        self.patient_name = patient_name
        self.prescribed_medicines = prescribed_medicines
        self.is_verified = False
    
    def verify_prescription(self):
        """Verify prescription"""
        self.is_verified = True
        return True
    
    def display_prescription(self):
        """Display prescription details"""
        medicines_str = ', '.join([f"{m['name']} - {m['quantity']} units" for m in self.prescribed_medicines])
        return f"Prescription ID: {self.prescription_id}, Doctor: {self.doctor_name}, Patient: {self.patient_name}, Medicines: {medicines_str}, Verified: {self.is_verified}"
    
    def __str__(self):
        return f"Prescription({self.prescription_id}, {self.patient_name})"
    
    def __repr__(self):
        return f"Prescription(id={self.prescription_id}, patient={self.patient_name}, verified={self.is_verified})"
    
    def to_dict(self):
        return {
            'prescription_id': self.prescription_id,
            'doctor_name': self.doctor_name,
            'patient_name': self.patient_name,
            'prescribed_medicines': self.prescribed_medicines,
            'is_verified': self.is_verified
        }
