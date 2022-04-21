import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'newyork': 'new_york_city.csv',
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

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    City_options = ['chicago','washington','newyork']
    while True:
        city = input('please select a city you want to analyze from Washington,Chicago and Newyork:\n\n').lower()
        if city in City_options:
            print('it seems you have requested data from {}.if this is true please type in yes otherwise type in no.\n'.format(city))
            answer = input().lower()
            if answer == "no":
                print('\nWrong Request?\n Try Again!\n')
            else:
                print('\nParsing data from {}.....\n'.format(city))
                break
        else:
            print('Error! INVALID CITY\n')

    # get user input for month (all, january, february, ... , june)
    month_options = ['jan','feb','mar','apr','may','jun']
    filter_op = input('Enter -all- to analyse months or -choice- to choose month\n').lower()
    if filter_op == "all":
        month = "all"
    else:
        while True:
            month = input('\nplease choose your desired month by entering the corresponding three-letter abbreviation i.e jan for january, feb for february, marc for march ..etc .\n\n').lower()
            if month in month_options:
                break
            else:
                print('INVALID MONTH\n')

        # get user input for day of week (all, monday, tuesday, ... sunday)
    day_options = ['mon','tue','wed','thu','fri','sat','sun']
    day_filter = ('Enter -all- to analyse all days or -choice- to choose day\n').lower()
    if day_filter == 'all':
        day = 'all'
    else:
        while True:
            day = input('\nplease enter abbreviation of desired day of the week as mon/tue/wed/thu/fri/sat/sun\n\n').lower()
            if day in day_options:
                break
            else:
                print('ERROR!INVALID DAY')

    print('-'*40)
    return city, month, day



#load file into dataframe
def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    #convert start Time column to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['Week day'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    #filter by month
    if month != 'all':
        month_options = ['jan','feb','mar','apr','may','jun']
        month =month_options.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week
    if day != 'all':
        day_options = ['mon','tue','wed','thu','fri','sat','sun']
        day = day_options.index(day)
        # filter by day of week to create the new dataframe
        df = df[df['Week day'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    most_month = df['month'].mode()
    print('the most common month of travel is:',most_month)
    # display the most common day of week
    most_day = df['Week day'].mode()
    print('the most common weekday of travel is:',most_day)
    # display the most common start hour
    most_hour = df['hour'].mode()
    print('the most common start hour is:',most_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mst_start_station = df['Start Station'].mode()
    print('the most used start station is :',mst_start_station)
    # display most commonly used end station
    mst_end_station = df['End Station'].mode()
    print('the most used end station is :',mst_end_station)
    # display most frequent combination of start station and end station trip
    df['Start - End'] = df['Start Station'] + "-" +df['End Station']
    mst_frq_comb = df['Start - End'].mode()
    print('the most frequent combination of start and stop stations is:',mst_frq_comb)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    TTD = df['Trip Duration'].sum()
    print ('the total trip duration is :',TTD)

    # display mean travel time
    ATD = df['Trip Duration'].mean()
    print('the average trip duration is :',ATD)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print(user_type)
    # Display counts of gender
    if 'Gender' in df.columns:
        genders = df['Gender'].value_counts()
        print(genders)
    else:
        print('no available data for Gender')
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        print('the earliest birth year is :',int(earliest_year))
    else:
        print('no available data for Birth Year')
    if 'Birth Year' in df.columns:
        most_recent_year = df['Birth Year'].max()
        print('the most recent year is:',int(most_recent_year))
    else:
        print('no available data for Birth Year')
    if 'Birth Year' in df.columns:
        mst_cmn_birthyear = df['Birth Year'].mode()
        print('the most common birthyear is :',mst_cmn_birthyear)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def see_five(df):
    '''
    prompt the user if they want to see 5 lines of raw data,
    Display that data if the answer is 'yes',
    Continue iterating these prompts and displaying the next 5 lines of raw data at each iteration,
    Stop the program when the user says 'no' or there is no more raw data to    display.
    '''
    view_data = input('Would you like to view the first five rows of the data? Please Enter either yes or no\n\n').lower()
    start_view = 0
    while view_data == 'yes':
        print (df.iloc[start_view:(start_view+5)])
        start_view += 5
        view_data = input('would you like to see the next five? enter yes or no\n')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        see_five(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
