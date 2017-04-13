# hadoop-project

##Weather system

This application reads the values of _daily.csv_ file which has the data of maximum and minimum temperatures of on a

particular date in cincinnati.

1. Open the url of the application http://myweathersystem.ddns.net/historical/.

2. This displays all the __dates__ whose information has been recorded.

3. A new record can be added to the database by using post to the same address and giving data in json format as

      {
      
        "DATE": "new date"
        
        "TMAX": "max temp on the date"
        
        "TMIN": "min temp on the date"
        
      }

4. The data on a particular date can be retreived by adding the date in format <YYYYMMDD> at the end of the address.

   eg: http://myweathersystem.ddns.net/historical/20130101

5. The data can be deleted by using _delete_ method and giving the date to be deleted in format <YYYYMMDD> at the end of   
   
   address. 
   
   eg:  http://myweathersystem.ddns.net/historical/20130101 

6. Open the url of the application http://myweathersystem.ddns.net/forecast.

7. Select a __date__ to get the forecast and click on forecast button.

8. The application displays a plot of maximum and minimum temperatures for consecutive 5 days starting from given date.

9. The application doesn't reload whole page when we select a different date but just gets data of different dates using 
   
   ajax.
