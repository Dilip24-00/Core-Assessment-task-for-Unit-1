
# This line imports the requests library so the program can retrieve data from the TimeAPI website.
import requests

# This line imports the datetime and timezone classes so the program can work with dates, times, and UTC values.
from datetime import datetime, timezone

# This line sends a GET request to the TimeAPI website so the program can retrieve the current date and time.
response = requests.get("https://timeapi.io/api/Time/current/zone?timeZone=America/Chicago")

# This line converts the API response into a Python dictionary so the program can access the returned information.
data = response.json()

# This line assigns "N/A" to the client_ip variable because the TimeAPI service does not provide the client's IP address.
client_ip = "N/A"

# This line extracts the dateTime value from the JSON response so the program can perform date calculations.
date_time_string = data["dateTime"]

# This line converts the dateTime string into a datetime object so the program can use Python's date functions.
current_datetime = datetime.fromisoformat(date_time_string)

# This line calculates the current day of the year so the program can display and use this value later.
day_of_year = current_datetime.timetuple().tm_yday

# This line retrieves the current UTC date and time so the program can display the universal time.
utc_datetime = datetime.now(timezone.utc)

# This line converts the current datetime into a Unix timestamp so the program can recreate the current date later.
unixtime = int(current_datetime.timestamp())

# This line displays the client IP value so the required assignment output is produced.
print("client_ip:", client_ip)

# This line displays the current day of the year so the required assignment output is produced.
print("day_of_year:", day_of_year)

# This line displays the current UTC date and time so the required assignment output is produced.
print("utc_datetime:", utc_datetime)

# This line displays the Unix timestamp so the required assignment output is produced.
print("unixtime:", unixtime)

# This line stores the day of the year when the course began so the program can calculate course progress.
begin_course_day = datetime(2026, 6, 8).timetuple().tm_yday

# This line creates a datetime object from the Unix timestamp so the program can calculate the current date.
now_date = datetime.fromtimestamp(unixtime)

# This line calculates the current day of the year so it can be compared with the course start day.
now_day = now_date.timetuple().tm_yday

# This line calculates the number of days that have passed since the course began so the current Unit can be determined.
days_elapsed = now_day - begin_course_day

# This line divides the elapsed days by seven and removes the decimal portion so the completed Units are calculated.
completed_units = days_elapsed // 7

# This line displays the completed Units so the user can see current course progress.
print(f"You have completed {completed_units} Units of 8.")
