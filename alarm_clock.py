import time
from datetime import datetime, timedelta
import emoji_util
import winsound

def run():
    print("\n\nLaunching Alarm Clock module...")

    # Welcome message
    print(f"""
    {emoji_util.CLOCK} Welcome to the Alarm Clock module of your toolkit!
    Set a time, name your alarm, and wait for it to ring. Press Ctrl+C anytime to cancel.
    """)

    # Loop until valid time input is given
    while True:
        try:
            alarm_time_str = input("Set alarm time (HH:MM, 24-hour format): ").strip()
            # Validate format
            alarm_time_obj = datetime.strptime(alarm_time_str, "%H:%M").time()
            break
        except ValueError:
            print(f"{emoji_util.CROSS} Invalid format. Please use HH:MM (24-hour).")

    alarm_name = input("Enter a name for the alarm: ").strip() or "Unnamed Alarm"

    # Compute full datetime of alarm
    now = datetime.now()
    alarm_datetime = datetime.combine(now.date(), alarm_time_obj)

    # If time has passed, schedule it for next day
    if alarm_datetime < now:
        alarm_datetime += timedelta(days=1)

    print(f"\n{emoji_util.BEDTIME} Alarm '{alarm_name}' is set for {alarm_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{emoji_util.HOURGLASS} Countdown will display below. Press Ctrl+C anytime to cancel.\n")

    try:
        while True:
            now = datetime.now()
            remaining = alarm_datetime - now

            if remaining.total_seconds() <= 0:
                print(f"\n{emoji_util.CLOCK} ALARM: {alarm_name}! Time's up!\n")
                # Beep 10 times
                for _ in range(10):
                    winsound.Beep(1000, 500)
                    time.sleep(0.3)
                break
            
            # Show countdown in HH:MM:SS
            hours, remainder = divmod(int(remaining.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            print(f"\r⏳ Time remaining: {hours:02d}:{minutes:02d}:{seconds:02d}", end="")
            time.sleep(1)

    except KeyboardInterrupt:
        print(f"\n{emoji_util.STOP} Alarm cancelled by user.")

