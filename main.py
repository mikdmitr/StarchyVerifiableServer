#!/bin/python3

#
# Complete the 'subscription_summary' function below.
#

def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):
    """
    Parameters:
      months_subscribed: How many months each account purchased.
      ad_free_months: How many months each account paid for ad free viewing.
      video_on_demand_purchases: How many Videos on Demand each account purchased.
    """
    print("Welcome to the Ada+ Account Dashboard")
    print()

    
    # Write your code here




if __name__ == '__main__':    
    months_subscribed = []
    ad_free_months = []
    video_on_demand_purchases = []
    
    header = input().strip()

    while header == "months_subscribed:":
        line = input().strip()
        try:
            months_subscribed.append(int(line))
        except ValueError:
            header = line

    while header == "ad_free_months:":
        line = input().strip()
        try:
            ad_free_months.append(int(line))
        except ValueError:
            header = line

    while header == "video_on_demand_purchases:":
        try:
            line = input().strip()

            video_on_demand_purchases.append(int(line))
        except EOFError:
            header = None
            
    subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases)