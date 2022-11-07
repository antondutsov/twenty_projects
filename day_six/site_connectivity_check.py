"""
    This is basically a program
    who check if specified url has
    a ping, ergo is up and running
"""

import urllib.request as urllib


def connectivity_checker(url):
    print("Checking connectivity...")

    response = urllib.urlopen(url)
    print("Connected to", url, "succesfully")
    print("The response code was: ", response.getcode())


print("This is a site connectivity checker program\n")

input_url = input("Input the url of the site: ")

connectivity_checker(input_url)
