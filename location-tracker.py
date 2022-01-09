import pygeoip as geo
import gmplot as gm
import webbrowser
import os

loc_dat = geo.GeoIP('GeoLiteCity.dat')

print("Location Tracker using IP/URL")
print("Program Coded in Python")

print("")

print("1. Complete Location Lookup [IP]")
print("2. Website Server Record Lookup [URL]")
print("3. Organization/Business Lookup [URL]")
print("4. Physical Location Tracker [IP]")
print("5. Extras")
print("0. Exit")

print("")

choice = int(input("Enter your choice: "))

print("")

if choice == 1:
    ip = str(input("Enter IP Address: "))

    lookup = loc_dat.record_by_addr(ip)
    print("")
    print("Below is the Summary of the Given IP Address:")
    for key, val in lookup.items():
        print('%s : %s' % (key, val))

elif choice == 2:
    url = str(input("Enter URL: https://"))

    lookup = loc_dat.record_by_name(url)
    print("")
    print("Below is the Summary of the given URL:")
    for key, val in lookup.items():
        print('%s : %s' % (key, val))

elif choice == 3:
    url = str(input("Enter URL: https://"))

    lookup = loc_dat.time_zone_by_name(url)
    print("")
    print("Organization Base Location:", lookup)

elif choice == 4:
    print("Please choose from the options below according to the information you know:")
    print("")
    print("1. Track Location using Latitude & Longitude.")
    print("2. Track Location using IP Address")
    print("0. Exit")

    choice2 = int(input("Enter your choice (1/2/0): "))
    apikey = ''                                                 # apikey='Your API Key here'

    if choice2 == 1:
        print("Enter Latitude & Longitude below: ")
        lat = float(input("Enter Latitude: "))
        lon = float(input("Enter Longitude: "))
        map_plot = gm.GoogleMapPlotter(lat, lon, 13, apikey=apikey)
        map_plot.draw('map.html')
        print("Opening browser now...")
        map_file = 'file:///' + os.getcwd() + '/' + 'map.html'
        webbrowser.open_new_tab(map_file)

    elif choice2 == 2:
        ip = str(input("Enter IP Address: "))
        lookup = geo.GeoIP("GeoLiteCity.dat")
        data = lookup.record_by_name(ip)
        lat = data['latitude']
        lon = data['longitude']
        map_plot = gm.GoogleMapPlotter(lat, lon, 13, apikey=apikey)
        map_plot.draw('map.html')
        print("Opening browser now...")
        map_file = 'file:///' + os.getcwd() + '/' + 'map.html'
        webbrowser.open_new_tab(map_file)

    elif choice2 == 0:
        print("Program Exited.")
        quit()

    else:
        print("Invalid Choice Try Again!!!")
        quit()

elif choice == 5:
    print("Extras:")

    print("")

    print("1. Readme")
    print("2. Licence")
    print("3. Github Profile")
    print("4. Other Projects")
    print("5. My Blog")
    print("0. Exit")

    print("")

    choice3 = int(input("Enter your choice: "))

    if choice3 == 1:
        print("")

        print("Python Project designed by Kaif Shaikh.")
        print("Technology Used: Pure Python")
        print("3rd Party Modules Used: pygeoip & gmplot")
        print("Using this program user can lookup accurate location with the help of raw data like IP Addresses, "
              "Latitude & Longitude or Website URL. Also with the help of IP Address or Latitude & Longitude user can "
              "plot the precise location over Google Maps.")
        print("Note: Before running the program make sure to insert your Google Cloud API Key associated with Google "
              "Maps in the 'API Variable'")

    elif choice3 == 2:
        print("")

        print("Copyright 2022 Kaif Shaikh")

        print("")

        print("Permission is hereby granted, free of charge, to any person obtaining a copy of this software and ")
        print("associated documentation files (the 'Software'), to deal in the Software without restriction, ")
        print("including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, ")
        print("and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, ")
        print("subject to the following conditions: The above copyright notice and this permission notice shall be ")
        print("included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED 'AS IS', ")
        print("WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF ")
        print("MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS ")
        print("OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF ")
        print("CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR ")
        print("OTHER DEALINGS IN THE SOFTWARE.")

    elif choice3 == 3:
        webbrowser.open('https://github.com/kaifshaikhhhh/', new=2)

    elif choice3 == 4:
        webbrowser.open('https://linktr.ee/kaif.projects/', new=2)

    elif choice3 == 5:
        webbrowser.open('https://kaifshaikhhhh.github.io/', new=2)

    elif choice3 == 0:
        quit()

    else:
        print("Invalid Option Try Again!")
        quit()

elif choice == 0:
    quit()

else:
    print("Invalid Option Try Again!")
    quit()
