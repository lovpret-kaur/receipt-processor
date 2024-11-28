import math

def calculate_points(receipt):
    points = 0
    
    # 1. Points for alphanumeric characters in retailer name
    retailer = receipt['retailer']
    points += sum(c.isalnum() for c in retailer)
    
    # 2. Points for round dollar total
    total = float(receipt['total'])
    if total.is_integer():
        points += 50

    # 3. Points for total as a multiple of 0.25
    if total % 0.25 == 0:
        points += 25

    # 4. Points for items
    items = receipt['items']
    points += (len(items) // 2) * 5

    # 5. Points for item descriptions
    for item in items:
        description = item['shortDescription'].strip()
        if len(description) % 3 == 0:
            price = float(item['price'])
            points += math.ceil(price * 0.2)

    # 6. Points for odd purchase date
    purchase_date = receipt['purchaseDate']
    day = int(purchase_date.split('-')[-1])
    if day % 2 == 1:
        points += 6

    # 7. Points for time between 2:00 PM and 4:00 PM
    purchase_time = receipt['purchaseTime']
    hour, minute = map(int, purchase_time.split(':'))
    if 14 <= hour < 16:
        points += 10

    return points
