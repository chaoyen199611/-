# NSYSU CSE Bachelor's Degree Project
## Team Member
* 黃兆延
* 蔡昀燁
* 陳柏翰
## Youbike Crawler
### Function
* Get dataset of the [Kaohsiung Youbike Station Real-time Information Platform](http://od-oas.kcg.gov.tw/api/service/Get/b4dd9c40-9027-4125-8666-06bef1756092)
* Turn dataframe into `.csv` file
    * Store dataset in `data_before_preprocessing` folder
    * If folder not exist, program will execute `mkdir`
* Automatically pull dataset with specific period
* Function Expected
    * Dynamic modified the period when pulling dataset
    * Drawing dynamic statistic graph when pulling dataset
### Setup
install `schedule`, `json`, `pandas` package for python
```sh
pip install schedule
pip install json
pip install pandas
```
git clone repository from github
```sh
git clone https://github.com/chaoyen199611/CSE_project.git
```

### Usage
```sh
python main.py               // Default period=10 minutes
python main.py -sch <i>      //set period with <i> minutes   
```
