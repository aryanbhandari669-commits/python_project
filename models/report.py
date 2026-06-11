from datetime import datetime

class Report:
    """
    Report class to manage various reports
    """
    def __init__(self, report_id, report_type):
        self.report_id = report_id
        self.report_type = report_type  # daily_sales, monthly_sales, stock, expiry, profit_loss
        self.generated_date = datetime.now().strftime("%Y-%m-%d")
        self.data = []
    
    def generate_report(self, data):
        """Generate report from data"""
        self.data = data
        return True
    
    def export_report(self, format='csv'):
        """Export report in specified format"""
        if format == 'csv':
            return self._export_csv()
        elif format == 'json':
            return self._export_json()
        return None
    
    def _export_csv(self):
        """Export as CSV"""
        csv_content = f"Report ID: {self.report_id}\n"
        csv_content += f"Report Type: {self.report_type}\n"
        csv_content += f"Generated Date: {self.generated_date}\n\n"
        
        if self.data:
            keys = self.data[0].keys() if isinstance(self.data[0], dict) else []
            csv_content += ','.join(keys) + '\n'
            for item in self.data:
                if isinstance(item, dict):
                    csv_content += ','.join(str(v) for v in item.values()) + '\n'
        
        return csv_content
    
    def _export_json(self):
        """Export as JSON"""
        import json
        return json.dumps({
            'report_id': self.report_id,
            'report_type': self.report_type,
            'generated_date': self.generated_date,
            'data': self.data
        }, indent=2)
    
    def __str__(self):
        return f"Report({self.report_id}, {self.report_type})"
    
    def __repr__(self):
        return f"Report(id={self.report_id}, type={self.report_type}, records={len(self.data)})"
    
    def to_dict(self):
        return {
            'report_id': self.report_id,
            'report_type': self.report_type,
            'generated_date': self.generated_date,
            'data': self.data
        }
