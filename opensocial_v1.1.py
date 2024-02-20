# pylint: disable=missing-docstring
import concurrent.futures
import requests


# COLOUR PRINTING FUNCTION
def outer_func(colour):
    def inner_function(msg):
        print(f'{colour}{msg}')
    return inner_function


# Constants
GREEN = outer_func('\033[92m')
YELLOW = outer_func('\033[93m')
RED = outer_func('\033[91m')
WEBSITES:list[str] = ['ifttt.com/p/', 'ebay.com/usr/', 'twitch.tv/' ,'quora.com/profile/', 'linkedin.com/in/', 'snapchat.com/add/','instagram.com/','reddit.com/user/','facebook.com/','twitter.com/','youtube.com/','plus.google.com/s//top','reddit.com/user/','pinterest.com/','github.com/','flickr.com/people/','steamcommunity.com/id/','vimeo.com/','soundcloud.com/','disqus.com/by/','medium.com/@','vk.com/','about.me/','imgur.com/user/','flipboard.com/@','slideshare.net/','fotolog.com/','open.spotify.com/user/','mixcloud.com/','scribd.com/','badoo.com/en/','patreon.com/','bitbucket.org/','dailymotion.com/','etsy.com/shop/','cash.me/','behance.net/','goodreads.com/','instructables.com/member/','keybase.io/','kongregate.com/accounts/','angel.co/','last.fm/user/','dribbble.com/','codecademy.com/','en.gravatar.com/','pastebin.com/u/','foursquare.com/','roblox.com/user.aspx?username=','gumroad.com/','wattpad.com/user/','canva.com/','creativemarket.com/','trakt.tv/users/','buzzfeed.com/','houzz.com/user/','blip.fm/','wikipedia.org/wiki/User:','news.ycombinator.com/user?id=','deviantart.com/','codementor.io/','reverbnation.com/','designspiration.net/','bandcamp.com/','colourlovers.com/love/']


# Banner
def banner():
    RED(r'''
 ________  ________  _______   ________   ________  ________  ________  ___  ________  ___          
|\   __  \|\   __  \|\  ___ \ |\   ___  \|\   ____\|\   __  \|\   ____\|\  \|\   __  \|\  \         
\ \  \|\  \ \  \|\  \ \   __/|\ \  \\ \  \ \  \___|\ \  \|\  \ \  \___|\ \  \ \  \|\  \ \  \        
 \ \  \\\  \ \   ____\ \  \_|/_\ \  \\ \  \ \_____  \ \  \\\  \ \  \    \ \  \ \   __  \ \  \       
  \ \  \\\  \ \  \___|\ \  \_|\ \ \  \\ \  \|____|\  \ \  \\\  \ \  \____\ \  \ \  \ \  \ \  \____  
   \ \_______\ \__\    \ \_______\ \__\\ \__\____\_\  \ \_______\ \_______\ \__\ \__\ \__\ \_______\
    \|_______|\|__|     \|_______|\|__| \|__|\_________\|_______|\|_______|\|__|\|__|\|__|\|_______|
                                            \|_________|                                            
  
  By SeranoxSecurity //Origin Credit: w3w3w3                                                                                                  

                                                                                                    
  ''')

def search(username: str):
    GREEN(f'[+] Searching for username: {username}')
    GREEN('[+] Open Social v1.00 is working')

    count = 0
    match = True

    for url in WEBSITES:
        try:
            r = requests.get(f'https://{url}{username}')
        except requests.exceptions.ConnectionError:
            print("ConnectionError occured")

        if r.status_code == 200:
            if match:
                GREEN('[+] FOUND MATCHES')
                match = False

            YELLOW(f'\n{url} - {r.status_code} - OK')

            if username in r.text:
                GREEN(f'POSITIVE MATCH: USERNAME:{username} - text has been detected in URL.')

            else:
                RED(f'POSITIVE MATCH: USERNAME:{username} - text has NOT been detected in URL.')

            count += 1


    total = len(WEBSITES)
    GREEN(f'FINISHED: A total of {count} MATCHES found out of {total} websites.')

def main():
    banner()
    username = input('\033[31m{+} Enter username:')    
    search(username)

if __name__ == '__main__':
    main()
