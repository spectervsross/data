import billboard
import calendar 
import csv
from datetime import date, timedelta
from pandas import DataFrame,Series

# Get chart date
year = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]

for i in year:
    year = i
    c = calendar.TextCalendar(calendar.SUNDAY)
    for m in range(1,13):
        for x in c.itermonthdays(year,m):
            if x != 0:                                      #calendar constructs months with leading zeros (days belongng to the previous month)
                day = date(year,m,x)
                if day.weekday() == 1 or day.weekday() == 3: #if its Tuesday or Thursday
                #    print ("%s-%s-%s" % (year,m,x))
                    chart = billboard.ChartData('r-b-hip-hop-songs', date=day)
                    day_edit = ("%s-%s-%s" % (year,m,x))
                    # Get No.1 song
                    song = chart[0]
                    song_title = song.title
                    song_artist = song.artist
                    #result = [day_edit,song_artist, song_title]

                    result = {'Date' : [day_edit], 'Artist' : [song_artist] , 'Song' : [song_title] }
                    

                    df = DataFrame(result)
                    #print(df)
                    df.to_csv("chart.csv", mode='a', header=False)

                    '''
                    f = open('test2.csv','a', encoding='utf-8', newline='')
                    writer=csv.writer(f,lineterminator='\n')

                    for row in result:
                        writer.writerow([row(0)])
                        row_1 = row[1]
                        print(row_1)
                    f.close()
                    
                
                print(song_title)
                print(song_artist)
                print(day)
                '''