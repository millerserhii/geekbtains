
time_sec = int(input("Enter time in seconds "))

hours = int(time_sec/3600)
minutes_float = float(f"{(time_sec/3600 - hours)*60:.3f}")
minutes  = int((time_sec/3600 - hours)*60)
seconds = int((minutes_float-minutes)*60)

print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}")

