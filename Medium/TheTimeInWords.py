words = ["o' clock",'one','two','three','four','five','six','seven','eight','nine',
         'ten','eleven','twelve','thirteen','fourteen','quarter','sixteen','seventeen',
         'eighteen','nineteen','twenty','twenty one','twenty two','twenty three','twenty four',
         'twenty five','twenty six','twenty seven','twenty eight','twenty nine','half']

hour = int(raw_input())
minute = int(raw_input())

if minute > 30:
    hour += 1
if hour == 13:
    hour == 1

if minute == 0:
    print words[hour] + ' ' + words[minute]
elif minute == 1:
    print words[minute] + ' minute past ' + words[hour]
elif minute == 15 or minute == 30:
    print words[minute] + ' past ' + words[hour]
elif (minute >= 2) and (minute <=30):
    print words[minute] + ' minutes past ' + words[hour]
elif (minute == 45):
    print words[15] + ' to ' + words[hour]
elif (minute == 59):
    print words[1] + ' minute to ' + words[hour]
elif (minute > 30):
    print words[60-minute] + ' minutes to ' + words[hour]
