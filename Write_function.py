year = 2000     



def is_leap(year):
    leap = False
    if (year/4).is_integer()== True and (year/100).is_integer()== True and (year/400).is_integer()!= True:
        return  leap
    elif (year/4).is_integer()== True and (year/100).is_integer()!= True and (year/400).is_integer()!= True:
        return  not leap
    elif (year/4).is_integer()== True and (year/100).is_integer()== True and (year/400).is_integer()== True:
        return  not leap
    else:
        return leap


print(is_leap(year))
