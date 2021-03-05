#!/usr/bin/env python
# coding: utf-8

# In[1]:


# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# In[26]:


# write your update damages function here:
conversion = {"M": 1000000,
              "B": 1000000000}

updated_damages = []

def convert(x):
  for val in x:
    if val == 'Damages not recorded':
      updated_damages.append(val)
    elif "M" in val:
      new_val = val[:-1]
      new_valf = float(new_val) * 1000000
      updated_damages.append(new_valf)
    elif "B" in val:
      new_val = val[:-1]
      new_valf = float(new_val) * 1000000000
      updated_damages.append(new_valf)

convert(damages)

# print(updated_damages)


# In[3]:


# write your construct hurricane dictionary function here:

hurricanes = {}
def construct_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    for i in range(len(names)):
        hurricanes[names[i]] = {'Name': names[i], 
                                'Month': months[i], 
                                'Year': years[i],
                                'Max Sustained Wind': max_sustained_winds[i], 
                                'Areas Affected': areas_affected[i],
                                'Damage': updated_damages[i], 
                                'Death': deaths[i]}
    return hurricanes

construct_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)


# In[4]:


# write your construct hurricane by year dictionary function here:

def construct_dict_by_year(year):
    hurricanes_by_year = []
    for name in hurricanes:
        if hurricanes[name]['Year'] == year:
            hurricanes_by_year.append(hurricanes[name])
    return hurricanes_by_year


# In[25]:


# construct_dict_by_year(1932)


# In[24]:


# write your count affected areas function here:
areas_affected = {}

def count_affected_areas(dictionary):
    for name in dictionary:
        for area in dictionary[name]['Areas Affected']:
            if area in areas_affected:
                areas_affected[area] += 1
            else:
                areas_affected[area] = 1
    return areas_affected

affected_areas_count = count_affected_areas(hurricanes)

# print(affected_areas_count)


# In[7]:


# write your find most affected area function here:

# We then iterate through each area in our affected areas dictionary, 
# which we named affected_areas_count, and compare the count for each 
# area to max_area_count. If max_area_count is less than the count for an area, 
# max_area is updated to the current area and max_area_count is updated to the count for that area.

def most_affected_area(dictionary):
    max_area = ""
    max_area_count = 0
    for area, count in dictionary.items():
        if count > max_area_count:
            max_area_count = count
            max_area = area
    print(max_area, max_area_count)

most_affected_area(affected_areas_count)


# In[8]:


# write your greatest number of deaths function here:

def most_number_deaths(dictionary):
    max_mortality_cane = 'Cuba I'
    max_mortality = 0
    for name, data in dictionary.items():
        if data['Death'] > max_mortality:
            max_mortality = data['Death']
            max_mortality_cane = name
    print(dictionary[max_mortality_cane])

most_number_deaths(hurricanes)           


# In[18]:


# write your catgeorize by mortality function here:

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}

def rank_hurricane_mortality(dictionary):
    for name, data in dictionary.items():
        if data['Death'] == 0:
            hurricanes_by_mortality[0].append(name)
        elif data['Death'] <= mortality_scale[1]:
            hurricanes_by_mortality[1].append(name)
        elif data['Death'] <= mortality_scale[2]:
            hurricanes_by_mortality[2].append(name)
        elif data['Death'] <= mortality_scale[3]:
            hurricanes_by_mortality[3].append(name)
        elif data['Death'] <= mortality_scale[4]:
            hurricanes_by_mortality[4].append(name)
        else:
            hurricanes_by_mortality[5].append(name)

rank_hurricane_mortality(hurricanes)

print(hurricanes_by_mortality)


# In[10]:


# write your greatest damage function here:

def most_damage(dictionary):
    max_damage_cane = 'Cuba I'
    max_damage = 0
    for name, data in dictionary.items():
        if data['Damage'] == 'Damages not recorded':
            continue
        elif data['Damage'] > max_damage:
            max_damage = data['Damage']
            max_damage_cane = name
    print(dictionary[max_damage_cane])


most_damage(hurricanes)      


# In[23]:


# write your catgeorize by damage function here:

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000.0}

hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}



def rank_hurricane_damages(dictionary):
    for name, data in dictionary.items():
        if data['Damage'] == ('Damages not recorded' or 0):
            hurricanes_by_damage[0].append(dictionary[name])
        elif data['Damage'] <= damage_scale[1]:
            hurricanes_by_damage[1].append(dictionary[name])
        elif data['Damage'] <= damage_scale[2]:
            hurricanes_by_damage[2].append(dictionary[name])
        elif data['Damage'] <= damage_scale[3]:
            hurricanes_by_damage[3].append(dictionary[name])
        elif data['Damage'] <= damage_scale[4]:
            hurricanes_by_damage[4].append(dictionary[name])
        else:
            hurricanes_by_damage[5].append(dictionary[name])


rank_hurricane_damages(hurricanes)
# print(hurricanes_by_damage)

