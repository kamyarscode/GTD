# GTD

A script that can plot terrorism activities around the world on a map.

A project I embarked on to learn more about Pandas, databases, and manipulation in Python. I also wanted to put the regions affected the most by terrorism into perspective.

I wanted to create a schematic of the entire Earth with appropriate coordinates, but OpenStreetMap's servers could not handle my large 
request, so I decided to slice the world into the different regions depicted in the dataset. 
This led me to create helper methods to debug and figure out why I was getting wrong coordinates for the different regions. 
A full list of changes I made is included in errors.txt

Due to sensitivity of OSM and the export function, some of the region schematics are not entirely accurate. When plotted on, 
the image would not be in the correct area, so I adjusted the stretching values to get the image to match the plot. A couple coordinate points off should not pose much of an issue for this prototype. 

I also thought of automating the script so I wouldn't have to manually put in values for the different regions, but my IDE froze 
upon this change so I decided not to implement it.

Australia and Oceania have not yet been featured because I have no way of grabbing the proper size slice from OSM without killing their servers,
but it is something I plan on working on in the future. Perhaps by utilizing a service other than OSM


The link for the dataset can be found on https://www.kaggle.com/START-UMD/gtd and the link for the schematics is 
https://www.openstreetmap.org

<h1> TO DO: </h1>
  
  * Use Selenium to auto-export map from OSM or other service then implement into code.
  * Implement Australia and Oceania region
