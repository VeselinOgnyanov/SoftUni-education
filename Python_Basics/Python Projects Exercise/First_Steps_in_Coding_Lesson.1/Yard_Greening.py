price_per_sqr_meter = 7.61
discount = 0.18
greening_sqr_meters = float(input())
final_price = price_per_sqr_meter * greening_sqr_meters
total_discount = final_price * discount
final_greening_price = final_price - total_discount
print(f"The final price is {final_greening_price} lv.")
print(f"The discount is {total_discount} lv.")
