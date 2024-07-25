import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    mask1 = df['sex']=='Male' #Mask that choses just male data
    average_age_men = df[mask1].loc[:,'age'].mean() #Calcs the mean of the age data for the male masked data
    average_age_men = round(average_age_men,1)
    
    # What is the percentage of people who have a Bachelor's degree?
    mask2 = df['education']=='Bachelors' #Mask that picks out people with a bachelors degree
    percentage_bachelors = round((len(df[mask2])/len(df))*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    h_ed_df = df.loc[(df['education']=='Bachelors')|(df['education']=='Masters')|(df['education']=='Doctorate')]
    higher_education = len(h_ed_df)
    l_ed_df = df.loc[~((df['education']=='Bachelors')|(df['education']=='Masters')|(df['education']=='Doctorate'))]
    lower_education = len(l_ed_df)

    # percentage with salary >50K
    higher_education_rich = round(100*len(h_ed_df.loc[(h_ed_df['salary']=='>50K')])/len(h_ed_df),1)
    lower_education_rich = round(100*len(l_ed_df.loc[(l_ed_df['salary']=='>50K')])/len(l_ed_df),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers_df = df.loc[(df['hours-per-week']==min_work_hours)]
    num_min_workers = len(num_min_workers_df)

    rich_percentage = round(100*len(num_min_workers_df.loc[(num_min_workers_df['salary']=='>50K')])/num_min_workers,1)

    # What country has the highest percentage of people that earn >50K?
    w = df['native-country'].value_counts()#All nationalities with how many people
    w.index #This is a list of all the nationalities
    
    wlist = w.index.tolist()#convert w.index to a Python list
    data_list = [] #Empty list
    for value in range(len(wlist)):
        index=wlist[value]#This is the nation
        mask1 = df['native-country']==index#
        df1 = df[mask1]#Data frame of a single nation
        mask2 = df1['salary']=='>50K'
        df2 = df1[mask2]#Data frame of a single nation plus only >50k salary
        number = round(100*len(df2)/len(df1),1)#The percentage of people of given origin with >50K salary
        data_list.append(number)#Append to list
    
    max_index = data_list.index(max(data_list))#The index for max from wlist
    
    
    highest_earning_country = wlist[max_index]
    highest_earning_country_percentage = max(data_list)

    # Identify the most popular occupation for those who earn >50K in India.
    india_df = df.loc[(df['native-country']=='India')] #dataframe of India only
    india_df2 = india_df.loc[(df['salary']=='>50K')]#dataframe of India with >50K salary
    profesions = india_df2['occupation'].value_counts().index #The index names for the occupation series of India
    occlist = india_df2['occupation'].value_counts().to_list()#A list of values for each occupation for India >50K
    ind = occlist.index(max(occlist)) #The index of the top profession
    
    top_IN_occupation = profesions[ind]#The top Indian proffesion for >50K

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
