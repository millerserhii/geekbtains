
time_sec = int(input("Enter time in seconds "))

hours = int(time_sec/3600)
minutes_float = float(f"{(time_sec/3600 - hours)*60:.3f}")
minutes  = int((time_sec/3600 - hours)*60)
seconds = int((minutes_float-minutes)*60)

if hours < 10:
    hours = f"0{hours}"
if minutes < 10:
    minutes = f"0{minutes}"
if seconds < 10:
    seconds = f"0{seconds}"

print(f"{hours}:{minutes}:{seconds}")

