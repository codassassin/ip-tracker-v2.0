from geolite2 import geolite2
import requests


class bColors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'


def banner():
    print(bColors.GREEN + '<<< IP-TRACKER v2.0>>>')
    print(bColors.RED + r'''
  _
 | |
 | |___
 |  _  \   _   _
 | |_)  | | (_) |
  \____/   \__, |
            __/ |
           |___/
                                        _                                                         _
                                       | |                                                       (_)
                  ____     ____     ___| |   ___ _   ______   ______    ___ _   ______   ______   _   _ ____
                 / ___\   /    \   /  _  |  / _ | | /  ____| /  ____|  / _ | | /  ____| /  ____| | | | |   | \
                | |____  |  ()  | |  (_| | | (_|| | \_____ \ \_____ \ | (_|| | \_____ \ \_____ \ | | | |   | |
                 \____/   \____/   \____/   \___|_| |______/ |______/  \___|_| |______/ |______/ |_| |_|   |_|
        ''')


class IpTracker:
    def __init__(self):
        self.docReader = geolite2.reader()
        banner()

        self.r = str(bColors.RED)
        self.g = str(bColors.GREEN)
        self.b = str(bColors.BLUE)
        self.y = str(bColors.YELLOW)

    def ownTracker(self):
        IpTrack = requests.get('https://api.ipify.org').text
        trackLocation = self.docReader.get(IpTrack)
        trackLocList = []
        if 'city' in trackLocation:
            city = (trackLocation['city']['names']['en'])
            trackLocList.append(city)
        else:
            trackLocList.append("NA")
        if 'continent' in trackLocation:
            continent = (trackLocation['continent']['names']['en'])
            trackLocList.append(continent)
        else:
            trackLocList.append("NA")
        if 'country' in trackLocation:
            country = (trackLocation['country']['names']['en'])
            trackLocList.append(country)
        else:
            trackLocList.append("NA")
        locationAccuracy = str(trackLocation['location']['accuracy_radius'])
        trackLocList.append(locationAccuracy)

        locationLatitude = str(trackLocation['location']['latitude'])
        trackLocList.append(locationLatitude)

        locationLongitude = str(trackLocation['location']['longitude'])
        trackLocList.append(locationLongitude)

        if 'time_zone' in trackLocation:
            locationTimeZone = (trackLocation['location']['time_zone'])
            trackLocList.append(locationTimeZone)
        else:
            trackLocList.append("NA")

        if 'code' in trackLocation:
            postalCode = (trackLocation['postal']['code'])
            trackLocList.append(postalCode)
        else:
            trackLocList.append("NA")

        registeredCountry = (trackLocation['registered_country']['names']['en'])
        trackLocList.append(registeredCountry)
        if 'subdivisions' in trackLocation:
            subdivisions = (trackLocation['subdivisions'][0]['names']['en'])
            trackLocList.append(subdivisions)
        else:
            trackLocList.append("NA")
        # print(trackLocation)
        # print(trackLocList)

        print('\n\n' + self.b + "<<<  NATIVE MACHINE IP TRACK REPORT  >>>")
        print(self.r + '* ' + self.b + 'public_ip: ' + self.g + IpTrack)
        if 'city' in trackLocation:
            print(self.r + '* ' + self.b + 'city: ' + self.g + trackLocList[0])
        if 'continent' in trackLocation:
            print(self.r + '* ' + self.b + 'continent: ' + self.g + trackLocList[1])
        if 'country' in trackLocation:
            print(self.r + '* ' + self.b + 'country: ' + self.g + trackLocList[2])
        print(self.r + '* ' + self.b + 'location: ')
        print('\t' + self.r + '↪ ' + self.y + 'accuracy_radius: ' + self.g + trackLocList[3])
        print('\t' + self.r + '↪ ' + self.y + 'latitude: ' + self.g + trackLocList[4])
        print('\t' + self.r + '↪ ' + self.y + 'longitude: ' + self.g + trackLocList[5])
        print('\t' + self.r + '↪ ' + self.y + 'time_zone: ' + self.g + trackLocList[6])
        print('\t' + self.r + '↪ ' + self.y + 'map: ' + self.g +
              f'https://www.google.co.in/maps/@{trackLocList[4]},{trackLocList[5]},15z?hl=en')
        print(self.r + '* ' + self.b + 'postal_code: ' + self.g + trackLocList[7])
        print(self.r + '* ' + self.b + 'registered_country: ' + self.g + trackLocList[8])
        if 'subdivisions' in trackLocation:
            print(self.r + '* ' + self.b + 'subdivisions: ' + self.g + trackLocList[9])

    def multiTracker(self, ipList):
        list = ipList.split(',')
        # print(list)
        lenList = len(list)
        i = 0
        while i < lenList:
            list[i] = str(list[i]).strip()
            trackLocation = self.docReader.get(list[i])
            trackLocList = []
            if 'city' in trackLocation:
                city = (trackLocation['city']['names']['en'])
                trackLocList.append(city)
            else:
                trackLocList.append("NA")
            if 'continent' in trackLocation:
                continent = (trackLocation['continent']['names']['en'])
                trackLocList.append(continent)
            else:
                trackLocList.append("NA")
            if 'country' in trackLocation:
                country = (trackLocation['country']['names']['en'])
                trackLocList.append(country)
            else:
                trackLocList.append("NA")
            locationAccuracy = str(trackLocation['location']['accuracy_radius'])
            trackLocList.append(locationAccuracy)

            locationLatitude = str(trackLocation['location']['latitude'])
            trackLocList.append(locationLatitude)

            locationLongitude = str(trackLocation['location']['longitude'])
            trackLocList.append(locationLongitude)

            if 'time_zone' in trackLocation:
                locationTimeZone = (trackLocation['location']['time_zone'])
                trackLocList.append(locationTimeZone)
            else:
                trackLocList.append("NA")

            if 'code' in trackLocation:
                postalCode = (trackLocation['postal']['code'])
                trackLocList.append(postalCode)
            else:
                trackLocList.append("NA")

            registeredCountry = (trackLocation['registered_country']['names']['en'])
            trackLocList.append(registeredCountry)
            if 'subdivisions' in trackLocation:
                subdivisions = (trackLocation['subdivisions'][0]['names']['en'])
                trackLocList.append(subdivisions)
            else:
                trackLocList.append("NA")
            # print(trackLocation)
            # print(trackLocList)
            print('\n\n' + self.b + '<<<  ' + str(list[i]) + ' TRACK REPORT' + '  >>>')
            print(self.r + '* ' + self.b + 'public_ip: ' + self.g + list[i])
            if 'city' in trackLocation:
                print(self.r + '* ' + self.b + 'city: ' + self.g + trackLocList[0])
            if 'continent' in trackLocation:
                print(self.r + '* ' + self.b + 'continent: ' + self.g + trackLocList[1])
            if 'country' in trackLocation:
                print(self.r + '* ' + self.b + 'country: ' + self.g + trackLocList[2])
            print(self.r + '* ' + self.b + 'location: ')
            print('\t' + self.r + '↪ ' + self.y + 'accuracy_radius: ' + self.g + trackLocList[3])
            print('\t' + self.r + '↪ ' + self.y + 'latitude: ' + self.g + trackLocList[4])
            print('\t' + self.r + '↪ ' + self.y + 'longitude: ' + self.g + trackLocList[5])
            print('\t' + self.r + '↪ ' + self.y + 'time_zone: ' + self.g + trackLocList[6])
            print('\t' + self.r + '↪ ' + self.y + 'map: ' + self.g +
                  f'https://www.google.co.in/maps/@{trackLocList[4]},{trackLocList[5]},15z?hl=en')
            print(self.r + '* ' + self.b + 'postal_code: ' + self.g + trackLocList[7])
            print(self.r + '* ' + self.b + 'registered_country: ' + self.g + trackLocList[8])
            if 'subdivisions' in trackLocation:
                print(self.r + '* ' + self.b + 'subdivisions: ' + self.g + trackLocList[9])

            i += 1


if __name__ == '__main__':
    tracker = IpTracker()

    print('''
    \nEnter the mode of IP tracking:
        1. Track IP of the native machine
        2. Track custom IP(s)''')

    mode = input("\t\t:> ")
    
    if mode == '1':
        tracker.ownTracker()
    elif mode == '2':
        ipList = str(input("\nEnter the IP address(s) (e.g. '5.199.143.202, 109.70.100.45, 42.110.211.117'): "))
        tracker.multiTracker(ipList)
