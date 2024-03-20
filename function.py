def toCounter2(decimal):
    time = abs(int(decimal))
    minute = int((abs(decimal) - time) * 60)
    second = round((((abs(decimal) - time) * 60) - minute) * 60, 2)
            
    if decimal < 0:
        time = f"-{time}"

    return f"{time} j {minute} m {second} d"
		
def toDegree2(decimal):
    degree = abs(int(decimal))
    minute = int((abs(decimal) - degree) * 60)
    second = round((((abs(decimal) - degree) * 60) - minute) * 60, 2)
    
    if decimal < 0:
        degree = f"-{degree}"
        
    dms = f"{degree}\u00b0 {minute}\u2032 {second}\u2033"
    
    return dms

def toTime2(decimal):
    degree = abs(int(decimal))
    minute = int((abs(decimal) - degree) * 60)
    second = round((((abs(decimal) - degree) * 60) - minute) * 60, 2)
    
    if decimal < 0:
        degree = f"-{degree}"
        
    dms = f"{degree}:{minute}:{second}"
    
    return dms
	
def toDecimal(degree, minute, second, check):
    decimal = degree + (minute / 60) + (second / 3600)
    
    if check is False:
        decimal = 0 - decimal
    
    return decimal
    