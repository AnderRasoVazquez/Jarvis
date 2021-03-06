from colorama import Fore
from utilities.GeneralUtilities import print_say
import mapps


def main(MEMORY, self):
    location = MEMORY.get_data('city')  # Will return None if no value
    if location is None:
        loc = str(location)
        city = mapps.getLocation()['city']
        print_say("It appears you are in " +
              city + " Is this correct? (y/n)", self, Fore.RED)

        try:
            i = raw_input()
        except:
            i = input()
        if i == 'n' or i == 'no':
            print_say("Enter Name of city: ", self)
            try:
                i = raw_input()
            except:
                i = input()
            city = i

        mapps.weather(str(city))

        MEMORY.update_data('city', city)
        MEMORY.save()
    else:
        loc = str(location)
        city = mapps.getLocation()['city']
        if city != loc:
            print_say("It appears you are in " + city +
                  ". But you set your location to " + loc, self, Fore.RED)
            print_say("Do you want weather for " +
                  city + " instead? (y/n)", self, Fore.RED)
            try:
                i = raw_input()
            except:
                i = input()
            if i == 'y' or i == 'yes':
                try:
                    print_say("Would you like to set " + city +
                          " as your new location? (y/n)", self, Fore.RED)
                    try:
                        i = raw_input()
                    except:
                        i = input()
                    if i == 'y' or i == 'yes':
                        MEMORY.update_data('city', city)
                        MEMORY.save()

                    mapps.weather(city)
                except:
                    print_say("I couldn't locate you", self, Fore.RED)
            else:
                try:
                    mapps.weather(loc)
                except:
                    print_say("I couldn't locate you", self, Fore.RED)
        else:
            try:
                mapps.weather(loc)
            except:
                print_say("I couldn't locate you", self, Fore.RED)
