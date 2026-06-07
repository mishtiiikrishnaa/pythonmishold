sec=int(input("enter seconds: "))
print("days: ", sec//(24*60*60), ", hours: ", (sec%(24*60*60))/(60*60), ", and minutes: ", (sec%(24*60*60))/(60*60), "and seconds: ", (sec%(24*60*60)/(60*60))/60)