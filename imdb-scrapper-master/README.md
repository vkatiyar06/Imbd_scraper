# imdb-scrapper

### Getting started  

This script scrapes imdb to fetch information about TV series.  
Also deals with mailing this info to the user_email account mentioned.
  
#### Prerequisite
Follow the following steps to get your script running:-  
  * you need to have python installed in your local machine.  
  * Download the zip file of this repositiory and extract it in your workspace.  
  * connecting to database - open [**savetodb.py**](https://github.com/shubham-tin/imdb-scrapper/blob/master/savetodb.py)  
    enter your database credentials:-
    ```   
          host="localhost",  
          user="root",  
          passwd="*****",  
          db="tvseries"  
      ```        
  
  * Before running make small change to [**'mailing.py'**](https://github.com/shubham-tin/imdb-scrapper/blob/master/mailing.py) file by entering your account credentials:- **username** and **password** and then save the file.  
  
  <img src="https://github.com/shubham-tin/imdb-scrapper/blob/master/crendentials.png" alt="image" height="200px" width="400px"/>
  
  
 #### Installing packages  
 
 * To install smtplib:   
   **smtplib** is a python module which prvides a method to send email. 
 > $ pip install smtplib  

 * To install mysql.connector:  
 > $ pip install mysql.connector  
 ```
  mysql.connector establishes a connection between python script and mysql database  
  mysql.conncetor make use of it's 'connect' method to connect to database.
 ```  
 
 
  
  
  * cd to the repo folder from command line.  
  * Then from the command line  run:  
  
  
  > **$ python imdbscrapper.py**  
  
  



