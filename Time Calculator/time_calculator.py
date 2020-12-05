#This is my solution to the Time Calculator Problem in FCC's Scientific Computing with Python.
#You can view the original question and my repl solution @ https://repl.it/@atelicious/FCC-time-calculator-solution


def add_time(start, duration, starting_day= ' '):

  start_time_h, start_time_m, start_time_ampm = start.replace(' ',':').split(':')
  duration_time_h, duration_time_m = duration.split(':')
    
  half_day = 720 #half day is 720 minutes
  full_day = half_day*2
  default_day = False 

  if starting_day == ' ':              # checks whether or not the user passed an argument for day
      default_day = True               # if user passed a value, the function will use it as a starting day               
      starting_day = 'monday'          # if not then 'monday will be used
  else:
      starting_day = starting_day

  if start_time_ampm == 'AM' and int(start_time_h) < 12:                           #this block of code will transform
      start_time_totalmin = int(start_time_h)*60 + int(start_time_m)               #the time from 12hr to 24hr time
  elif start_time_ampm == 'AM' and int(start_time_h) >= 12:                        #and convert it into minutes
      start_time_totalmin = 0 + int(start_time_m)
  elif start_time_ampm == 'PM' and int(start_time_h) < 12:
      start_time_totalmin = half_day + int(start_time_h)*60 + int(start_time_m)
  elif start_time_ampm == 'PM' and int(start_time_h) >= 12:
      start_time_totalmin = half_day + int(start_time_m)
 
  duration_time_totalmin = int(duration_time_h)*60 + int(duration_time_m)         #this will add the start time and the added time
    
  time_total = start_time_totalmin + duration_time_totalmin
  day_counter = time_total // full_day                                            #this will count how many days the added time is

  week_dict = {'monday' : 1, 'tuesday' : 2, 'wednesday' : 3, 'thursday': 4, 'friday' : 5, 'saturday' : 6, 'sunday' : 7}

  x = week_dict[starting_day.lower()] + day_counter    

  while x > 7:             # this will check where the additional day will be on a mon-sun week
      diff = x - 7
      x = 0
      x = x + diff

  x_state = list(week_dict.keys())[list(week_dict.values()).index(x)] 

  while time_total >= full_day:             #this will check where the total time will be on a 24hr clock
      time_diff = time_total - full_day
      time_total = 0
      time_total = time_total + time_diff

  if time_total in range(0, 719):      #if time_total is from 0 (00:00) to 719 (11:59 AM) then time is in AM
        z_state = 'AM'
  elif time_total in range(720, 1440): #if time_total is from 720 (12:00PM) to 1440 (12:00 AM) then time is in PM
      z_state = 'PM'

  if z_state == 'AM':
      if time_total in range(0,60) or time_total in range(1440, 1440+60): #this converts 00:00 to 12:00 if it happens
          time_hr = 12
          time_min = time_total % 60
      else:
          time_hr = time_total // 60
          time_min = time_total % 60
  else:
      if time_total in range(720,780) or time_total in range(1440, 1440+60): #this converts 00:00 to 12:00 if it happens
          time_hr = 12
          time_min = (time_total -half_day) % 60
      else:
          time_hr = (time_total - half_day) // 60
          time_min = (time_total -half_day) % 60

  if default_day == True: # if the user didn't passed an argument for starting_day, this will be the returned values:
      if day_counter == 0:
          return f'{time_hr}:{time_min:02d} {z_state}'  #return value if the new time is still in the same day
      elif day_counter == 1:
          return f'{time_hr}:{time_min:02d} {z_state} (next day)' #return value if the new time is tommorow
      elif day_counter > 1:
          return f'{time_hr}:{time_min:02d} {z_state} ({day_counter} days later)' #return value if the new time is in n days later
  else:
      if day_counter == 0: #if the user passed an argument for starting_day, this will be the returned values:
          return f'{time_hr}:{time_min:02d} {z_state}, {x_state.title()}' #return value if the new time is still in the same day
      elif day_counter == 1:
          return f'{time_hr}:{time_min:02d} {z_state}, {x_state.title()} (next day)' #return value if the new time is tommorow
      elif day_counter > 1:
          return f'{time_hr}:{time_min:02d} {z_state}, {x_state.title()} ({day_counter} days later)' #return value if the new time is in n days later