exam_hour = int(input())
exam_minute = int(input())
arrival_hour =  int(input())
arrival_minute =  int(input())

exam_hour *= 60
arrival_hour *= 60
total_exam_minutes = exam_hour + exam_minute
total_arrive_minutes = arrival_hour + arrival_minute

if total_arrive_minutes == total_exam_minutes or (total_exam_minutes - 30) <= total_arrive_minutes <= total_exam_minutes:
    print("On time")
elif total_arrive_minutes > total_exam_minutes:
    print("Late")
elif (total_exam_minutes - 30) > total_arrive_minutes:
    print("Early")

difference = abs(total_arrive_minutes - total_exam_minutes)
if (total_exam_minutes - 60) < total_arrive_minutes <= total_exam_minutes:
    print(f"{difference} minutes before the start")
elif total_arrive_minutes <= (total_exam_minutes - 60):
    hour = difference // 60
    minutes = difference % 60
    print(f"{hour}:{minutes:02d} hours before the start")
elif total_exam_minutes <= total_arrive_minutes < (total_exam_minutes + 60):
    print(f"{difference} minutes after the start")
elif total_arrive_minutes >= (total_exam_minutes + 60):
    hour = difference // 60
    minutes = difference % 60
    print(f"{hour}:{minutes:02d} hours after the start")