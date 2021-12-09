# CourseProject

## Search System For Hospital Transparency Data
Tony Law, Morgan Whitman, Aareana Reza

Healthcare costs make up one of individuals and employers largest expenses. Prices continue to rise and put burden on individuals and health plans. New legislation in recent years has required hospitals to provide standard prices on a publicly available websites. This data is accessible on hospital or health system websites but not easily accessible to individuals searching by service. 

This project allows users to query/search medical services ("shoppable" services are of particular interest) and returns a list of relevant treatments and hospitals with these reported services. Our code also has the additional functionality to input a city and limit the results of the search to hospitals within a certain city. We opted to comment out this due to the limited dataset. 

See below for the general flow of our code. 

![Screenshot](Hospital_Transparency_Flow_Chart.jpg)

### To Run Code

Requirements: 
* python 3.5
`pip install -r requirments.txt`

On command line, enter:
`python main.py`

Suggested treatments to search: "mri", "ct scans", "air", "transport", "ambulance"

### Dataset  

* dolthub Hospital Price Transparency [link](https://www.dolthub.com/repositories/dolthub/hospital-price-transparency)
* Kaggle Dataset hospital-price-transparency [link](https://www.kaggle.com/natesutton/hospitalpricetransparency?select=concept.csv)

### Future Improvements

Due to the limitations of the dataset we used, our search was limited to hospitals in North Carolina. There significantly larger datasets available but they also needed to be purchased or granted access. 

* Develop a larger dataset
* Add Ranker function that utilized the Patient information obtained from searches
* Rank the hospitals, import Health Grade dataset

### Please see documentation pdf for additional information as per requirements of CS410 project