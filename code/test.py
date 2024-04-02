from datetime import datetime

def get_time_difference(start_time, end_time):
  # Convert timestamps to datetime objects
  start_datetime = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S.%f")
  end_datetime = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S.%f")
  # Calculate the difference as a timedelta object
  time_delta = end_datetime - start_datetime
  # Return the difference in seconds
  return time_delta

# Example usage with the provided timestamps
time_difference = get_time_difference("2024-01-30 13:26:50.701606", "2024-03-30 13:26:52.596551")
print({time_difference})