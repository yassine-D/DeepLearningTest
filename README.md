## DeepLearningTest

### Description:
  This project contains the code to connect to <b>"an instagram account created just for this task"</b>
  <ul>
  <li>Search for instagram posts related to a specified topic</li>
  <li>Scrap the data from posts and load it into .csv file and MongoDB database</li>
  </ul>

#### Project tree:

```
├── scraped_data
│   └── scraped_data.csv    #The .csv file contains the scrapped intagram posts
├── insta_connector.py      #The code to establish a connection to the newly created instagram account for test
├── main.py                 # main function 
├── mongoDB_connector.py    # Contains the code to establish a connection to the local mongodb server       
├── requirements.txt        # Requirement file contains the dependencies for the project
├── scraping.py             # Connect to instagram account and scrap posts related to a given topic
├── utils.py                # Contains util regex functions to extract meaninful informations and patterns
```
  
  
  
  
