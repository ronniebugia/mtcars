# Motor Trend Car Road Tests Visualization App
Data visualization for Motor Trend Car Road Tests from https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html

## About the App
The app visualizes data from the Motor Trend Car Road Tests dataset available online. There is a radar plot assessing the performance of 
the indvidual car models. You can choose the model being plotted from a dropdown menu. 

There is also a bar chart comparing the attributes of each car model. You can choose the attribute being compared from another dropdown menu.

## Getting Started
You will need the following dependencies to run the app: <br />
dash <br />
dash_table <br />
pandas <br />
numpy <br />
plotly 

## To Run the App
Clone this repository on your computer then cd into repository

```
git clone https://github.com/ronniebugia/mtcars.git
cd mtcars
```

Install dependencies from requirements.txt

```
pip install -r requirements.txt
```

You can then run the app with

```
python app.py
```
    
## Update History
2019/03/07
9:57pm PST <br />
New Additions <br />
-Added Radar Plot showcasing attributes for car based on input from dropdown menu <br />
-Added bar graph comparing the attributes for models, the attribute is chosen from a dropdown menu 

## Future Plans
Planned future updates include <br />
-Adding more cars to the dataset <br />
-An image gallery to go along with dataset

