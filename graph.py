import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

raw_data = {'metode': ['IDS Snort', 'String Matching', 'Aho Corasick'],
        'Snort_IDS': [56.47, 0, 0],
        'String_Matching': [0, 0.08715, 0],
        'Aho_Corasick': [0, 0, 0.00696]}
df = pd.DataFrame(raw_data, columns = ['metode', 'Snort_IDS', 'String_Matching', 'Aho_Corasick'])
df
# Setting the positions and width for the bars
pos = list(range(len(df['Snort_IDS']))) 
width = 0.25 
    
# Plotting the bars
fig, ax = plt.subplots(figsize=(5,5))

# Create a bar with pre_score data,
# in position pos,
plt.bar(pos, 
        #using df['pre_score'] data,
        df['Snort_IDS'], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#EE3224', 
        # with label the first value in first_name
        label=df['metode'][0]) 

# Create a bar with mid_score data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos], 
        #using df['mid_score'] data,
        df['String_Matching'],
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#F78F1E', 
        # with label the second value in first_name
        label=df['metode'][1]) 

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*2 for p in pos], 
        #using df['post_score'] data,
        df['Aho_Corasick'], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#FFC222', 
        # with label the third value in first_name
        label=df['metode'][2]) 

# Set the y axis label
ax.set_ylabel('Nilai (%)')

# Set the chart's title
ax.set_title('Perbandingan Nilai Rata-rata FPR dalam %')

# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['metode'])

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(df['Snort_IDS'] + df['String_Matching'] + df['Aho_Corasick'])] )

# Adding the legend and showing the plot
plt.legend(['Snort IDS', 'String Matching', 'Aho Corasick'], loc='upper left')
plt.grid()
plt.show()
