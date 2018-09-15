from classes import Datreader,Report
get_report = Report('weather.dat',0,1)
day_with_min_temp_diff = get_report.get_the_answer()
print(day_with_min_temp_diff)