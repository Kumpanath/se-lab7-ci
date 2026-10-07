def total_price(items, delivery_fee):
    """
    คำนวณราคารวมคำสั่งซื้ออาหาร

    items: รายการอาหารในรูปแบบ [(ชื่ออาหาร, ราคา), ...]
    delivery_fee: ค่าส่ง
    """
    return sum(price for name, price in items) + delivery_fee
  items = [("ข้าวกะเพรา", 50),("ชาเย็น", 30)]
  print(total_price(items, 10))
