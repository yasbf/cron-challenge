# cron-challenge

We have a set of tasks, each running at least daily, which are scheduled with a simplified cron. We want to find when each of them will next run.

The scheduler config looks like this:

`30 1 /bin/run_me_daily`

`45 * /bin/run_me_hourly`

`* * /bin/run_me_every_minute`

`* 19 /bin/run_me_sixty_times`

The first field is the minutes past the hour, the second field is the hour of the day and the third is the command to run. For both cases * means that it should run for all values of that field. In the above example run_me_daily has been set to run at 1:30am every day and run_me_hourly at 45 minutes past the hour every hour. The fields are whitespace separated and each entry is on a separate line.

We want you to write a command line program that when fed this config to stdin and a simulated 'current time' in the format HH:MM as command line argument outputs the soonest time at which each of the commands will fire and whether it is today or tomorrow. When the task should fire at the simulated 'current time' then that is the time you should output, not the next one.

For example given the above examples as input and the simulated 'current time' command-line argument 16:10 the output should be

`1:30 tomorrow - /bin/run_me_daily`

`16:45 today - /bin/run_me_hourly`

`16:10 today - /bin/run_me_every_minute`

`19:00 today - /bin/run_me_sixty_times`

## Developed features

1. Script will silently ignore hour > 24 and minute > 60 and keep going.
2. If script launched with Log arguments ==> Show error message in these two cases
3. if line is empty and not last line, script will silently ignore it.
4. if line is missing one argument, script will silently ignore it.
5. If script launched with Log arguments ==> Show error message with missing argument
6. script will use current time if argument "simulated time" is missing.
7. scrip will silently ignore other in-line arguments.

## Next features

1. Add proper argument order handling
2. Add possibility to pass input.txt as an argument
   e.g: pyhton minicron.py -c input.txt
3. Use Exception instead of print 
4. Better use of functions and global variables for reusability

## Running

script requires Python3
From the top level directory (cron-challenge)
```
cat input.txt | python3 minicron.py
cat input.txt | python3 minicron.py 16:10
cat input.txt | python3 minicron.py Log
cat input.txt | python3 minicron.py 16:10 Log
```

### Arguments
Script file name [required]

Time in HH:MM format [optional]

Log: show some extras logs [optional]
