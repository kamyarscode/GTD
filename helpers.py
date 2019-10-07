import pandas as pd

class Helpers:

    #create our dataframe and drop NaN values
    df = pd.read_csv('gtdataset.csv', encoding = 'ISO-8859-1', low_memory = False)
    dfkeep = df[['longitude', 'latitude', 'provstate' ,'city', 'region_txt']].set_index('region_txt').dropna()

    def __init__(self, name):
        self.name = name

    def get_df_info(self):
        return self.dfkeep.sort_values('region_txt')

    #write to notepad for debugging purposes
    def write_to_notepad(self):
        with open('testpad.txt', 'a+', encoding='ISO-8859-1') as f:
            f.write(Helpers.get_row_by_region(self).to_string())
            f.close()

    #get rows that match user entered cities
    def get_row_by_city(self,city):
        self.dfkeep.reset_index(inplace = True)
        dfkeep = self.dfkeep.set_index('city')
        rows = dfkeep.loc[f'{city}', : ]
        return rows

    def get_row_by_region(self):
        rows = self.dfkeep.loc[f'{self.name}', : ]
        return rows

    #primarily a debugger method which came in handy many times
    #get the furthest west and east or north and south coordinates and cities based on latitude or longitude index
    def get_extremes(self, min, max, index):
        self.dfkeep.reset_index()
        dfkeep = self.df[['longitude', 'latitude', 'provstate', 'city', 'region_txt']].set_index(f'{index}')
        rows = [dfkeep.loc[min, : ],dfkeep.loc[max, : ]]

        if index == 'longitude':
            return (f'Your western most point is : {rows[0]} \n Your eastern most point is {rows[1]}')
        elif index == 'latitude':
            return (f'Your southern most point is : {rows[0]} \n Your northern most point is {rows[1]}')
        return 'Did not understand'

    #create the boundary box to use as export guide
    def get_bbox(self):
        bbox = [self.longitude.min(), self.longitude.max(),
                self.latitude.min(), self.latitude.max()]
        return bbox


#search = (g.dfkeep[(g.dfkeep['city'] == 'Berlin') & (g.dfkeep['region_txt'] == 'Eastern Europe')])
#search['region_txt'] = search['region_txt'].replace('Eastern Europe', 'Western Europe')


