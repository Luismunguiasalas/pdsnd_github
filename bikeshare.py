import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
ALL_MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    valid_cities = {'chicago', 'new york city', 'washington'}
    valid_months = {'january', 'february', 'march', 'april', 'may', 'june', 'all'}
    valid_days = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'}
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True:
        try:
            input_city = input("Enter one of the city names (chicago, new york city, washington) that you would like to analyze: ").lower()
            if (input_city == '' or (input_city not in valid_cities)):
                raise exception()
            input_month = input("Enter the month name, e.g., (january, february, ..., june) to filter by month. Enter 'all' to apply no month filters: ").lower()
            if (input_month == '' or (input_month not in valid_months)):
                raise exception()
            input_day = input("Enter the day name, e.g., (monday, tuesday, ..., sunday) to filter by day. Enter 'all' to apply no day filters: ").lower()
            if (input_day == '' or (input_day not in valid_days)):
                raise exception()
        except:
            print('-'*20, 'Start of Error Message', '-'*20)
            print('\nOnly enter alphabetical characters for your choice of city, month, and day. Any other special character or number is not valid \n')
            print('For example, this is a valid entry: \n city: chicago \n month: June \n day: tuesday \n\n Please try again.... \n')
            print('Note: The first six months are the only valid months, i.e., anything after June is not valid \n')
            print('-'*20, 'End of Error Message', '-'*20, '\n')            
        else:
            break
    print('-'*40)

    return input_city, input_month, input_day


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        target_month_index = ALL_MONTHS.index(month) + 1
        df = df[df['month'] == target_month_index]
    if day != 'all':
        df = df[df['day'] == day.capitalize()]
    return df


def time_stats(df):
    """
        Displays statistics on the most frequent times of travel.
        Args:
            (obj) df - Pandas DataFrame object
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    month_index = df['month'].mode()[0]
    print('Most Common Month:', ALL_MONTHS[month_index-1].capitalize(), '\n')
    
    day = df['day'].mode()[0]
    print('Most Common Day:', day, '\n')
    
    df['hour'] = df['Start Time'].dt.hour
    print('Most Common Start Hour:', df['hour'].mode()[0], '\n')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
        Displays statistics on the most popular stations and trip.
        Args:
            (obj) df - Pandas DataFrame object        
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', start_station, '\n')

    end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', end_station, '\n')
    
    most_frequent = df[['Start Station', 'End Station']].mode().iloc[0]
    print("Most Frequent Combination of Start Station and End Station:\nStart Station: ", most_frequent[0], '\nEnd Station: ' , most_frequent[1],"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
        Displays statistics on the total and average trip duration.
        Args:
            (obj) df - Pandas DataFrame object
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    minutes = total_travel_time / 60
    hours = minutes / 60
    print('Total Travel Time:', total_travel_time, 'seconds =', minutes, 'minutes =', hours, 'hours' )

    mean_travel_time = df['Trip Duration'].mean()
    minutes = mean_travel_time / 60
    hours = minutes / 60
    print('Mean Travel Time:', mean_travel_time, 'seconds =', minutes, 'minutes =', hours, 'hours' )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
        Displays statistics on bikeshare users.
        Args:
            (obj) df: dataframe
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    count_user_types = df['User Type'].value_counts()
    print('Count By User Types:\n', count_user_types , '\n')

    try:
        count_gender = df['Gender'].value_counts()
        print('Count By Gender:\n', count_gender, '\n')
    except:
        print('This dataset does Not contain any gender data. Therefore a calculation will not be computed for Gender')

    try:
        early_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print('Earliest Birth Year:', int(early_birth), '\n')
        print('Most Recent Birth Year:', int(recent_birth), '\n')
        print('Most Common Birth Year:', int(common_birth), '\n')
    except:
        print('This dataset does Not contain any birthday data. Therefore a calculation will not be computed for Birthday')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(iterable, n_rows):
    """
        Display the raw table data for every 'n_rows' number of rows
        Args:
            (obj) df - Pandas DataFrame obj
            (int) n_rows - number of rows to display
        yield:
            (obj) df - Pandas DataFrame of size equal to n_rows
    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    i = 0
    ln = len(iterable)
    while i < ln:
        next_five = next_five = input('\nWould you like to see 5 rows of raw data? Enter "yes" or "no"\n').lower()
        if next_five == 'yes':
            yield iterable[i : i + n_rows]
            i += n_rows
        else:
            break 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        print('\nYour filters:\nCity:', city, '\nMonth:', month, '\nday:',day, '\n')
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        for i in raw_data(df,5):
            print(i)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()