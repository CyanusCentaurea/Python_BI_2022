#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re


# In[2]:


# TASK 1.1
def read_gff(path_to_gff):
    """.gff reader
    """
    df_gff = pd.read_csv(path_to_gff, sep='\t', comment='#',
                       names=['chromosome', 'sourse', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes'])
    return df_gff


# In[3]:


# reading rrna_annotation.gff
rrna_annotation = read_gff('rrna_annotation.gff')
rrna_annotation


# In[4]:


def read_bed6(path_to_bed):
    """.bed6 reader
    """
    df_bed = pd.read_csv(path_to_bed, sep='\t', comment='#',
                       names=['chromosome', 'start', 'end', 'name', 'score', 'strand'])
    return df_bed


# In[5]:


# reading rrna_annotation.gff
alignment = read_bed6('alignment.bed')
alignment


# In[6]:


def ribosome_type_finder(string):
    """Finds ribosome type in string
    """
    return re.search(r'(\d+S)', string)[0]


# In[7]:


# TASK 1.2
# creating a new data frame with only RNA type in attributes column
my_rrna_annotation = rrna_annotation.copy()
my_rrna_annotation['attributes'] = my_rrna_annotation['attributes'].apply(ribosome_type_finder, 0)
my_rrna_annotation


# In[8]:


# renaming column with only RNA type in new data frame
my_rrna_annotation.rename(columns={'attributes': 'RNA type'}, inplace=True)
my_rrna_annotation


# In[9]:


# TASK 1.3
# grouping annotation by chromosome and RNA type with counting RNA within one type
grouped_rrna_annotation = my_rrna_annotation.groupby(['chromosome', 'RNA type']).agg({'RNA type':'count'})
grouped_rrna_annotation = grouped_rrna_annotation.rename(columns={'RNA type': 'Count RNA types'}).reset_index()
grouped_rrna_annotation


# In[10]:


# building barplot for grouped_rrna_annotation
sns.set(rc={'figure.figsize':(11.7, 8.27),
           'axes.facecolor': 'white', 
             'axes.edgecolor': 'black',
            'xtick.minor.visible': True})
bar_plot_count_RNA_types = sns.barplot(x='chromosome', 
                                       y='Count RNA types', 
                                       hue='RNA type', 
                                       data=grouped_rrna_annotation)
sns.move_legend(bar_plot_count_RNA_types, "upper right")
bar_plot_count_RNA_types.grid(False)
bar_plot_count_RNA_types.tick_params(which='major', direction="out", left=True, bottom=True, width=1, size=3)
bar_plot_count_RNA_types.spines['left'].set_color('black')
bar_plot_count_RNA_types.spines['right'].set_color('black')
bar_plot_count_RNA_types.spines['top'].set_color('black')
bar_plot_count_RNA_types.spines['bottom'].set_color('black')
bar_plot_count_RNA_types.set_xticklabels(bar_plot_count_RNA_types.get_xticklabels(), rotation = 90)


# In[34]:


# TASK 1.4
# Performing the functions of the bedtools intersect with pandas. 
# Finding out how much rRNA was successfully assembled during the assembly process. 
# Outputing a table containing the original records about rRNA completely included in the assembly (not a fragment), 
# as well as a record about the contig in which this RNA is.
intersection = pd.merge(rrna_annotation, alignment, 
                   how='inner', 
                   left_on=['chromosome'], 
                   right_on=['chromosome'])
intersection


# In[12]:


intersection = intersection.query('start_y <= start_x')
intersection = intersection.query('end_y >= end_x') 
intersection.drop_duplicates()
intersection


# In[13]:


# TASK 2
# reading diffexpr_data.tsv.gz
diffexpr = pd.read_csv("diffexpr_data.tsv.gz", compression='gzip', sep='\t')
diffexpr


# In[14]:


# creating a data frame to build the plot: putting four different types of regulation in a separate column
sign_up = diffexpr.query('log_pval > 1.3 and logFC >= 0')
sign_up['Regulation']='Significantly upregulated'
nonsign_up = diffexpr.query('log_pval <= 1.3 and logFC >= 0')
nonsign_up['Regulation']='Non-significantly upregulated'
nonsign_down = diffexpr.query('log_pval <= 1.3 and logFC < 0')
nonsign_down['Regulation']='Non-significantly downregulated'
sign_down = diffexpr.query('log_pval > 1.3 and logFC < 0')
sign_down['Regulation']='Significantly downregulated'
my_diffexpr = pd.concat((sign_down,sign_up, nonsign_down, nonsign_up), axis=0)
my_diffexpr


# In[15]:


# building volcano plot
volcano = sns.scatterplot(data=my_diffexpr, 
                          x='logFC', 
                          y='log_pval', 
                          s=14, 
                          hue=my_diffexpr['Regulation'],
                          palette=['#1874CD', '#FF8247', '#008B00', '#B22222'],
                          linewidth=0)
volcano.grid(False)
volcano.spines['left'].set_color('black')
volcano.spines['right'].set_color('black')
volcano.spines['top'].set_color('black')
volcano.spines['bottom'].set_color('black')
volcano.spines['left'].set_linewidth(1.5)
volcano.spines['right'].set_linewidth(1.5)
volcano.spines['top'].set_linewidth(1.5)
volcano.spines['bottom'].set_linewidth(1.5)
volcano.minorticks_on()
volcano.tick_params(which='major', direction="out", left=True, bottom=True, width=1.5, size=6, color='black')
volcano.tick_params(which='minor', direction="out", left=True, bottom=True, width=1, size=3, color='black')
volcano.axhline(y=1.3, ls='--', c='grey', linewidth=1.7)
volcano.axvline(x=0, ls='--', c='grey', linewidth=1.7)
volcano.set_title('Volcano plot', size=24, style='italic', weight='bold')
volcano.set_xlabel('log$\mathbf{_2}$ (fold change)', size=14, style='italic', weight='bold')
volcano.set_ylabel('-log$\mathbf{_{10}}$ (p value corrected)', size=14, style='italic', weight='bold')
volcano.legend(shadow='right_bottom', markerscale=1.5, prop={'weight':'bold', 'size': 10})
volcano.text(6, 2, 'p value = 0.05', fontsize=15, color='grey', weight='bold')
volcano.annotate('UMOD', 
                 xy =(-10.7, 52.2),
                 xytext =(-10, 64),
                 weight='bold',
                 arrowprops = dict(facecolor ='red',
                                   shrink = 0.05,
                                  edgecolor='black'))
volcano.annotate('MUC7', 
                 xy =(-9.2, 2.2),
                 xytext =(-10, 15),
                 weight='bold',
                 arrowprops = dict(facecolor ='red',
                                   shrink = 0.05,
                                  edgecolor='black'))
volcano.annotate('ZIC5', 
                 xy =(4.3, 4.4),
                 xytext =(5, 20),
                 weight='bold',
                 arrowprops = dict(facecolor ='red',
                                   shrink = 0.05,
                                  edgecolor='black'))
volcano.annotate('ZIC2', 
                 xy =(4.6, 3),
                 xytext =(7, 11),
                 weight='bold',
                 arrowprops = dict(facecolor ='red',
                                   shrink = 0.05,
                                  edgecolor='black'))


# In[16]:


# TASK 3
# reading owid-covid-data.csv
covid = pd.read_csv("owid-covid-data.csv")
covid


# In[17]:


# estimating the NaNs
covid.isna().sum()


# In[18]:


# We see that in case of NaNs in total_cases column the most other columns are also shows NaNs.
covid.query('total_cases.isna()')


# In[19]:


covid['total_cases'].isna().sum()


# In[20]:


# So we can delete these rows and look at our data again.
# We see that total_cases NaNs were successfully removed as well as NaN in several other columns of which we were wrote above.
# Now we have many NaNs in location column.
covid.drop(covid[covid.total_cases.isna()].index, inplace=True)
covid.isna().sum()


# In[21]:


# Have a look on them.
# We see that in these cases the three-letter iso encoding is not respected. 
covid.query('continent.isna()')


# In[22]:


# For our rough EDA we can sacrifice this number of rows. Removing them.
covid.drop(covid[covid.continent.isna()].index, inplace=True)
covid.isna().sum()


# In[23]:


# We see too much NaN rows or different deaths and mortality statistics, we can not remove them.
# We will not analyze these statistics in our EDA.
covid.query('excess_mortality.isna()')


# In[24]:


# We see 3843 NaNs in people_fully_vaccinated column.
covid['people_fully_vaccinated'].isna().sum()


# In[25]:


# For our rough EDA we can sacrifice this number of rows. Removing them.
covid.drop(covid[covid.people_fully_vaccinated.isna()].index, inplace=True)
covid.isna().sum()


# In[26]:


# Now our data became a bit cleaner and we can start analyzing it and building some plots.
# We can look at the largest reported number of Covid cases worldwide.
# We need to group data by location, define max of total cases by countries and separate the largest number of cases.
total_cases_location = covid.groupby('location').agg({'total_cases':'max'})
total_cases_location = total_cases_location.reset_index()
total_cases_location['total_cases'] /= 1000000
total_cases_location.drop(total_cases_location[total_cases_location.total_cases < 2].index, inplace=True)
total_cases_location.sort_values(by=['total_cases'], ascending=False, inplace=True)
total_cases_location


# In[27]:


# building barplot for grouped total_cases_location
total_cases_location_bar = sns.barplot(x='total_cases', 
                                       y='location',
                                       palette = sns.color_palette("Reds_d", len(total_cases_location))[::-1],
                                       data=total_cases_location)

total_cases_location_bar.set_title('The largest reported number of Covid cases by countries', size=14, style='italic', weight='bold')
total_cases_location_bar.set_xlabel('Total cases, m.', size=12)
total_cases_location_bar.set_ylabel('Country')
total_cases_location_bar

# Judging by the plot, we see that the USA is the leader in the total number of cases, 
# but we should not forget that this is the third country in terms of population in the world. 
# Moreover, this is a very developed country and we can assume that the incidence statistics are kept very strictly, 
# unlike, for example, Mexico or Philippines which also have a very high population, but not such a developed and
# centralized level of medicine.


# In[35]:


# Let's visualize and confirm our assumption about population.
# We need to group data by location again and by date, define max population by countries.
population_location = covid.groupby('location').agg({'population':'max'})
population_location = population_location.reset_index()
population_location['population'] /= 1000000
population_location.drop(population_location[population_location.population < 50].index, inplace=True)
population_location.sort_values(by=['population'], ascending=False, inplace=True)
population_location


# In[36]:


# building barplot for population_location
population_location_bar = sns.barplot(x='population', 
                                       y='location',
                                      color='blue',
                                      data=population_location)

population_location_bar.set_title('Countries with the highest population', size=14, style='italic', weight='bold')
population_location_bar.set_xlabel('Population, m.', size=12)
population_location_bar.set_ylabel('Country')
population_location_bar
# Indeed, Mexico and the Philippines, which we recalled, occupy a leading position in this list.


# In[38]:


# We also can look at new Covid cases daily in Europe (because we are actually in Europe!)
# We need to group data by location again and by date, define sum of new cases.
new_cases_monthly_Europe = covid.groupby(['location', 'date']).agg({'new_cases':'sum'})
new_cases_monthly_Europe = new_cases_monthly_Europe.rename(columns={'new_cases': 'New cases'}).reset_index()
new_cases_monthly_Europe['date'] = new_cases_monthly_Europe['date'].apply(pd.to_datetime, 0)
new_cases_monthly_Europe.sort_values(by=['date'], inplace=True)
new_cases_monthly_Europe = new_cases_monthly_Europe.merge(total_cases_location, 
                   how='inner', 
                   left_on=['location'], 
                   right_on=['location'])
new_cases_monthly_Europe = new_cases_monthly_Europe.iloc[:, :3].drop_duplicates()

# Then we need to leave only Europe countries in our data set.
new_cases_monthly_Europe = new_cases_monthly_Europe.query('location in ["France", "Germany", "United Kingdom", '
                                                          '"Italy", "Russia", "Spain", "Poland", "Belgium", "Greece", '
                                                          '"Ukraine", "Switzerland", "Czechia", "Denmark", "Romania", '
                                                          '"Slovakia", "Sweden"]') 
new_cases_monthly_Europe


# In[39]:


# building barplot for new_cases_monthly_Europe
new_cases_monthly_Europe_plot = sns.lineplot(x='date',
                                      y='New cases',
                                      hue='location',
                                             palette='bright',
                                             data=new_cases_monthly_Europe)
new_cases_monthly_Europe_plot.set_title('New Covid cases reported, Europe', size=14, style='italic', weight='bold')
new_cases_monthly_Europe_plot.set_xlabel('Months', size=11)
new_cases_monthly_Europe_plot.set_ylabel('New cases daily', size=12)

# We see approximately similar trends in the spread of the disease.
# An increase in the incidence is clearly visible with the advent of Omicron variant at the beginning of 2022. 
# The record jumps in incidence during this period in France (far over 200,000 people a day) and then (March, April) in Germany 
# are especially eye-catching, and these cases are confirmed by information from open sources.


# In[40]:


# Let's look at the level of vaccination.
# We need to group data by location again and define max of fully vaccinated people by countries.
fully_vaccinated_location = covid.groupby('location').agg({'people_fully_vaccinated':'max'})
fully_vaccinated_location = fully_vaccinated_location.reset_index()
fully_vaccinated_location['people_fully_vaccinated'] /= 1000000
fully_vaccinated_location.drop(fully_vaccinated_location[fully_vaccinated_location.people_fully_vaccinated < 10].index, inplace=True)
fully_vaccinated_location.sort_values(by=['people_fully_vaccinated'], ascending=False, inplace=True)
fully_vaccinated_location


# In[41]:


# building barplot for new_cases_monthly_Europe
fully_vaccinated_location_bar = sns.barplot(x='people_fully_vaccinated', 
                                       y='location',
                                       palette = sns.color_palette("Greens_d", len(fully_vaccinated_location))[::-1],
                                       data=fully_vaccinated_location)

fully_vaccinated_location_bar.set_title('Countries with the most fully vaccinated people', size=14, style='italic', weight='bold')
fully_vaccinated_location_bar.set_xlabel('People fully vaccinated, m.', size=12)
fully_vaccinated_location_bar.set_ylabel('Country')
fully_vaccinated_location_bar

# The plot shows that the most disciplined countries are China, India and USA. 
# But we should not rush to conclusions because there is a clear correlation with the population again. 
# After all, these are indeed the three leading countries in this parameter.


# The general conclusion that we can draw is that these data are very voluminous and interesting, 
# it requires special attention and a lot of time for a full-fledged analysis.


# In[ ]:




