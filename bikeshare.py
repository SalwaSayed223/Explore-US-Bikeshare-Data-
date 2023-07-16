import time
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_list=["chicago","new york city","washington"]
    city=input("enter a city name from those(chicago,new york city,washington): ").lower()
    while True:
        if city not in CITY_DATA.keys():
            print("name error:this city isnot one of determined cities")
            city=input("enter a city name from those(chicago,new york city,washington): ").lower()
            continue        
        else:
            break
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month_list=["january","february","march","april","may","june","all"]
    month_name=input("enter a month  from those (all,january,february,..,june):").lower()
    while True:
        if month_name not in month_list:
              print("name error : this month isnot one of given months")
              month_name=input("enter a month from those (all,january,february,..,june): ").lower()
              continue        
        else : 
            month=month_name
    
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list=["all","monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    day_name=input("enter a day of week(all,monday,tuesday,..,sunday):").lower()
    while True:
        if day_name  not in day_list:
            print("name error:this day isnot in given days")
            day_nam=input("enter a day of week(all,monday,tuesday,..,sunday):").lower()
            continue
        else: 
           day=day_name
           break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df=pd.read_csv(CITY_DATA[city])
    df["Start Time"]=pd.to_datetime(df["Start Time"])
    df["month name"]=df["Start Time"].dt.month_name()
    df["day name"]=df["Start Time"].dt.day_name()
    df["hour"]=df["Start Time"].dt.hour
    if month!="all":
        df=df[df["month name"]==month.title()]
        
    if day!="all":
        df=df[df["day name"]==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df["month name"].mode()[0]
    print("\nthe most common month is ",common_month,"\n")
    # TO DO: display the most common day of week
    common_day=df["day name"].mode()[0]
    print("\nThe most common day of week is",common_day,"\n")
    # TO DO: display the most common start hour
    common_hour=df["hour"].mode()[0]
    print("\nThe most common start hour is ",common_hour,"\n")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df["Start Station"].mode()[0]    
    print("\nThe most commonly used start station is ",common_start_station,"\n")
    # TO DO: display most commonly used end station
    common_end_station=df["End Station"].mode()[0]
    print("\nThe most commonly used end station ",common_end_station,"\n")
    # TO DO: display most frequent combination of start station and end station trip
    common_start_end=(df["Start Station"]+" "+df["End Station"]).mode()[0]    
    print("\nThe most frequent combination of start station and end station trip ",common_start_end,"\n") 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df["Trip Duration"].sum(axis=0)
    print("\nTotal travel time = ",total_travel_time,"\n")
    # TO DO: display mean travel time
    mean_travel_time=df["Trip Duration"].mean(axis=0)
    print("\nmean travel time = ",mean_travel_time,"\n") 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts=df["User Type"].value_counts()
    print("\ncounts of user types : ",user_type_counts,"\n")
    # TO DO: Display counts of gender
    try:
        
         gender_counts=df["Gender"].value_counts()
         print("\ncounts of gender = ",gender_counts,"\n")   
    except:
        print("gender is  unknown for that city")
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        
        earliest_birth_year=int(df["Birth Year"].min(axis=0,skipna=True))
        recent_birth_year=int(df["Birth Year"].max(axis=0,skipna=True))
        common_birth_year=int(df["Birth Year"].mode()[0])
        print("\nThe earliest year of birth is ",earliest_birth_year,"\n")
        print("\nThe most recent year of birth is",recent_birth_year,"\n")
        print("\nThe most common year of birth is ",common_birth_year,"\n")       
    except: 
        print("birth year is unknown for that city")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    '''
    Ask user to display 5 raws ofindividual trip data.
    returns:(str) view_data=yes or no
    '''
    
    view_data=input("\nwould you like to view 5 raws of individual trip data?Enter yes or no\n").lower()
    start_lock=0
    if view_data not in ["yes","no"]:
            print("\n incorrect ,please enter yes or no.\n")
            view_data=input("\nwould you like to view 5 raws of individual trip data?Enter yes or no\n").lower()
    elif view_data=="no":
        print("thank you")
    while view_data=="yes":
        print(df.iloc[start_lock:start_lock+5])
        start_lock+=5
        view_data=input("Do you want to continue?").lower()
        if view_data !="yes":
                        
                   print("thank you")
                   break
    
    
    
           
                        
                        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df) 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
