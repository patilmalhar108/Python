def calculate_attendance():
        total_days = int(input("Enter total number of working days: "))        
        absent_days = int(input("Enter total number of days absent: "))
        if total_days <= 0:
            print("Error: Total working days must be greater than zero.")
            return
        if absent_days < 0:
            print("Error: Absent days cannot be negative.")
            return
        if absent_days > total_days:
            print("Error: Absent days cannot exceed total working days.")
            return
        attended_days = total_days - absent_days
        percentage = (attended_days / total_days) * 100
        print(f"\nAttendance Percentage: {percentage:.2f}%")
        if percentage < 75:
            print("The student won't be able to attend exam.")
        else:
            print("The student is eligible to attend the exam.")