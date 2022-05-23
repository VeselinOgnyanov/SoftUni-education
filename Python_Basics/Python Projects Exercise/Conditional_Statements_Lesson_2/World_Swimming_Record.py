current_record = float(input())
distance = float(input())
sec_per_meter = float(input())

delay = (distance // 15) * 12.5
total_time = (distance * sec_per_meter) + delay

if total_time < current_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    seconds_more = current_record - total_time
    seconds_more = abs(seconds_more)
    print(f"No, he failed! He was {seconds_more:.2f} seconds slower.")