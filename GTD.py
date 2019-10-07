from helpers import Helpers
import matplotlib.patches as pat
import matplotlib.pyplot as plt
import os

##########
#---------------------- ** REGIONS ** ----------------------#
#Australasia & Oceania, Central America & Caribbean, Central Asia, East Asia, Eastern Europe,
#Middle East & North Africa, North America, South America, South Asia, Southeast Asia, Sub-Saharan Africa,
#Western Europe
##########

#count number of occurrences for each city
def get_count(df):
    return df['city'].value_counts()


regionList = [Helpers('North America'), Helpers('South America'), Helpers('Central America & Caribbean'), Helpers('Sub-Saharan Africa'),
              Helpers('Middle East & North Africa'), Helpers('Western Europe'), Helpers('Central Asia'), Helpers('South Asia'),
              Helpers('East Asia'), Helpers('Southeast Asia'), Helpers('Australasia & Oceania'), Helpers('Eastern Europe')]

name = regionList[0].name
DIR = 'D:\\Programming related\\Python Projects\\GTDdata\\schematics'
NAPATH = f'D:\\Programming related\\Python Projects\\GTDdata\schematics\\{name}.png'
naimage = plt.imread(NAPATH)



#Rows of region entries
regionInfo = regionList[0].get_row_by_region()
attacks = len(regionInfo)
#boundary coordinates for region
coordinates = Helpers.get_bbox(regionInfo)
#extreme points used for debugging and verification
extremes = regionList[0].get_extremes(coordinates[0],coordinates[1], 'longitude')
print (coordinates)
print (extremes)

os.chdir(DIR)
#create the plot
fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(regionInfo.longitude, regionInfo.latitude, zorder=1, alpha= 0.2, c='r', s=10)
ax.set_title(f'Terrorist Attacks in {name} Since 1970')
ax.set_xlim(coordinates[0],coordinates[1])
ax.set_ylim(coordinates[2],coordinates[3])

#left, right, bottom, top
ax.imshow(naimage, zorder = 0, extent = [coordinates[0], coordinates[1], coordinates[2], coordinates[3]], aspect = 'auto')
patch = pat.Patch(color = 'r', label= attacks)
plt.legend(handles=[patch], title = f'Number of Attacks in {name}')
plt.show()

