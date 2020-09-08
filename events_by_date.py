import urllib.request
import json
import requests


def fetch_events():
    url = 'http://open-api.myhelsinki.fi/v1/events/'
    data = requests.get(url).json()
    results = data['data']
    eventsArr = []
    print(type(data))
    print(len(data))
    for item in results:
        if item['event_dates']['starting_day'] == None:
            continue
        else:
            print(item['event_dates']['starting_day'])
            eventsArr.append(item['event_dates']['starting_day'][0:10])
    print(eventsArr)
    return eventsArr
# kuplalajittelu ideksi A < B? => vaihdetaan A ja B paikkaa


def main():
    arr = fetch_events()
    bubbleSort(arr)


def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
