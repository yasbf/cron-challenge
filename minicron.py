
#####################################################
# Enhancement :
#
# Add arguments order handling
# Pass input.txt as an argument
# add proper error handling (ex: case of empty input file)
#
#####################################################


import sys
import os
from datetime import datetime
os.system("clear")

# Get current time by default (in case of time not provided as argument)
args_now_time = datetime.now()
args_now_hour = int(args_now_time.strftime("%H"))
args_now_minute = int(args_now_time.strftime("%M"))

showLogs = False

def log(message):
    if showLogs:
        print(message)

def is_hour(hour):
    return False if hour >= 24 else True

def is_minute(minute):
    return False if minute >= 60 else True

input_lines_array = []
if len(sys.argv) == 2:
    # 2 args : file name + time OR Log
    # If second argument is "Log" ==> use current time & show logs
    showLogs = True if "Log" in sys.argv[1] else False

    # if second argument is time ==> use it and don't show logs
    if ":" in sys.argv[1]:
        args_now_time = sys.argv[1].split(':')
        args_now_hour = int(args_now_time[0])
        args_now_minute = int(args_now_time[1])

elif len(sys.argv) == 3:
    # 3 args : file name + time + log
    if "Log" in sys.argv[2]:
        showLogs = True
        args_now_time = sys.argv[1].split(':')
        args_now_hour = int(args_now_time[0])
        args_now_minute = int(args_now_time[1])
        if not is_hour(args_now_hour):
            raise Exception("invalid arg : hour is greater than 24")
        if not is_minute(args_now_minute):
            raise Exception("invalid arg : minute is greater than 60")
##############################

def main():
    # Read output of cat command
    for line in sys.stdin:
        input_lines_array.append(line)

    count = 0
    for line in input_lines_array:
        count += 1
        splitted_line_array = line.split(" ")
        scheduled_minute = 0
        scheduled_hour = 0

        # Check if line is well formatted (we have 3 parts)
        if len(splitted_line_array) == 3:
            splitted_line_array[2] = splitted_line_array[2].rstrip()
        else:
            log('Line #{0} : not correctly formatted'.format(count))
            continue

        # Get hour & minutes from file line and check them
        file_line_minute = splitted_line_array[0]
        file_line_hour = splitted_line_array[1]
        if file_line_minute.isnumeric():
            if not is_minute(int(file_line_minute)):
                log('Line #{0} : minute is greater than 60'.format(count))
                continue
        else:
            if not file_line_minute == '*':
                log('Line #{0} : minute must be an integer lower than 60 or an "*"'.format(count))
                continue

        if file_line_hour.isnumeric():
            if not is_hour(int(file_line_hour)):
                log('Line #{0} : hour is greater than 24.'.format(count))
                continue
        else:
            if not file_line_hour == '*':
                log('Line #{0} : minute must be an integer lower than 24 or an "*"'.format(count))
                continue

        scheduled_command = splitted_line_array[2]
        scheduled_day = 'toscheduled_day'

        if not file_line_hour == '*' and not file_line_minute == '*':
            scheduled_hour = int(file_line_hour)
            scheduled_minute = int(file_line_minute)

        if file_line_hour == '*' and not file_line_minute == '*':
            scheduled_minute = int(file_line_minute)
            if int(file_line_minute) > args_now_minute:
                scheduled_hour = args_now_hour
            else:
                scheduled_hour = args_now_hour + 1

        if file_line_minute == '*':
            if file_line_hour == '*':
                scheduled_minute = args_now_minute
                scheduled_hour = args_now_hour
            else:
                scheduled_minute = 00
                scheduled_hour = int(file_line_hour)
        if 24 <= scheduled_hour < 48:
            scheduled_hour = 00
            scheduled_day = 'tomorrow'
        if scheduled_hour > 48:
            log('Line #{0} : hour is greater than 24.'.format(count))

        if scheduled_hour < args_now_hour:
            scheduled_day = 'tomorrow'
        elif scheduled_hour == args_now_hour:
            if scheduled_minute < args_now_minute:
                scheduled_day = 'tomorrow'

        scheduled_minute = str(scheduled_minute).zfill(2) # convert back to string to display double zero

        print('{0}:{1} {2} - {3}'.format(scheduled_hour,scheduled_minute,scheduled_day,scheduled_command))


if __name__ == "__main__":
    main()
