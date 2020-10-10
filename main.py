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

    accountCounter = []
    accountCounter.append(int(len(months_subscribed)))
    accountCounter.append(int(len(ad_free_months)))
    accountCounter.append(int(len(video_on_demand_purchases)))

    accountsNumber=max(accountCounter)

    totalEarningsForAllAccounts=0.0

    totalEarnedFromAdFreeWatchingAndVideoOnDemand=0.0

    mostProfitableAccount=0

    mostProfitableAccountEarning=0.0

    i=0

    while i<accountsNumber :
      summaryOfEarningsForAccount=0.0
      EarnedFromSubscribed=0.0
      EarnedFromAdFreeWatching=0.0
      EarnedVideoOnDemand=0.0

      try:
        if months_subscribed[i]>=3:
          EarnedFromSubscribed=(months_subscribed[i]//3)*18.00+(months_subscribed[i]%3)*7.00
        else:
          EarnedFromSubscribed=months_subscribed[i]*7.00
      except:
        i=i

      try:
        EarnedFromAdFreeWatching=ad_free_months[i]*2.00
      except:
        i=i  

      try:
        EarnedVideoOnDemand=video_on_demand_purchases[i]*27.99
      except:
        i=i   

      summaryOfEarningsForAccount=EarnedFromSubscribed+EarnedFromAdFreeWatching+EarnedVideoOnDemand

      totalEarningsForAllAccounts=totalEarningsForAllAccounts+summaryOfEarningsForAccount

      totalEarnedFromAdFreeWatchingAndVideoOnDemand=totalEarnedFromAdFreeWatchingAndVideoOnDemand+EarnedFromAdFreeWatching+EarnedVideoOnDemand

      if(summaryOfEarningsForAccount>mostProfitableAccountEarning):
        mostProfitableAccountEarning=summaryOfEarningsForAccount
        mostProfitableAccount=i+1

      print()  

      print("Account ",i+1,"  made  $","%.2f" % summaryOfEarningsForAccount," total")

      print(">>> $","%.2f" % EarnedFromSubscribed," from monthly subscription fees")

      print(">>> $","%.2f" % EarnedFromAdFreeWatching," from Ad-free upgrades")   

      print(">>> $","%.2f" % EarnedVideoOnDemand," from Video on Demand purchases")  

      i+=1
    
    print()

    print("Combined all accounts made $","%.2f" % totalEarningsForAllAccounts ," total")

    print("Premium content (Ad- free watching and Video on Demand) made $","%.2f" % totalEarnedFromAdFreeWatchingAndVideoOnDemand," total")

    print()

    print("$","%.2f" % mostProfitableAccountEarning,"  was the most earned by any single account") 

    print("The accounts that earned the most were : #", mostProfitableAccount)





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
        except EOFError:   #you must press Ctrl+D to finish enter data
            header = None
            
    subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases)