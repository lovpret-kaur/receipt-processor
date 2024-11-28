receipts = {}

def store_receipt(receipt_id, points):
    receipts[receipt_id] = points

def get_points_by_id(receipt_id):
    return receipts.get(receipt_id)
