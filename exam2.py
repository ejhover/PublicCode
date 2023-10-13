# Emmet Hoversten
# hover114
# CSCI 1133 Section 050
# Exam 02 Problem 2
'''Import random module to be used when selecting dictionaries later'''
import random
class FloweringPlant:
    '''Parent class holding the variables to define a flowering plant'''
    def __init__(
            self, species, common_name,
            watering_interval=1, water_amount=2, days_since_water=0):
        ''''Initialize the variables needed for a watering plant within the class'''
        self.species = species
        self.common_name = common_name
        self.watering_interval = watering_interval
        self.water_amount = water_amount
        self.days_since_water = days_since_water
    def __repr__(self):
        '''Return the common name of the plant followed by the scientific name in parenthesis'''
        return f'{self.common_name} ({self.species})'
    def water(self):
        '''Water the plant and reset the days_since_water variable'''
        self.days_since_water = 0
    def check_water_needs(self):
        '''Returns bool of whether or not the plant needs to be watered'''
        return self.days_since_water>=self.watering_interval
class Succulent(FloweringPlant):
    '''Child class of FloweringPlant which also holds the amount of water stored in the plant'''
    def __init__(
            self, species, common_name,
            water_stored, watering_interval=1, water_amount=2,
            days_since_water=0):
        super().__init__(species, common_name, watering_interval, water_amount, days_since_water)
        self.water_stored = water_stored
    def __repr__(self):
        return super().__repr__() + f'; Water Stored: {self.water_stored}'
class Herb(FloweringPlant): 
    '''
    Child class of FloweringPlant which also stores:

    culinary_use: dictionary holding the plants different culinary uses
    medicinal_use: dictionary holding the plants different medicinal uses
    '''
    def __init__(
            self, species, common_name,
            medicinal_use, culinary_use, watering_interval=1,
            water_amount=2, days_since_water=0):
        super().__init__(species, common_name, watering_interval, water_amount, days_since_water)
        self.culinary_use = culinary_use
        self.medicinal_use = medicinal_use
    def __repr__(self):
        ran_cul = random.choice(list(self.culinary_use.keys()))
        ran_med = random.choice(list(self.medicinal_use.keys()))
        return super().__repr__()+"\n"+\
            f'Commonly used in {ran_cul} cuisine'\
            +f' in dishes such as {self.culinary_use[ran_cul]}.'+"\n"\
            f'Commonly used to treat {ran_med}. '\
            +f'One of its primary uses is in the treatment of {self.medicinal_use[ran_med]}.'
