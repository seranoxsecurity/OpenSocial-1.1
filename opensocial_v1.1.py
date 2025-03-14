import concurrent.futures
import requests
import random
from time import sleep
from concurrent.futures import ThreadPoolExecutor

# COLOUR PRINTING FUNCTION
def outer_func(colour):
    def inner_function(msg):
        print(f'{colour}{msg}')
    return inner_function

# Constants
GREEN = outer_func('\033[92m')
YELLOW = outer_func('\033[93m')
WEBSITES:list[str] = ['ifttt.com/p/', 'ebay.com/usr/', 'twitch.tv/' ,'quora.com/profile/', 'linkedin.com/in/', 'snapchat.com/add/','instagram.com/','reddit.com/user/','facebook.com/','twitter.com/','youtube.com/','plus.google.com/s//top','reddit.com/user/','pinterest.com/','github.com/','flickr.com/people/','steamcommunity.com/id/','vimeo.com/','soundcloud.com/','disqus.com/by/','medium.com/@','vk.com/','about.me/','imgur.com/user/','flipboard.com/@','slideshare.net/','fotolog.com/','open.spotify.com/user/','mixcloud.com/','scribd.com/','badoo.com/en/','patreon.com/','bitbucket.org/','dailymotion.com/','etsy.com/shop/','cash.me/','behance.net/','goodreads.com/','instructables.com/member/','keybase.io/','kongregate.com/accounts/','angel.co/','last.fm/user/','dribbble.com/','codecademy.com/','en.gravatar.com/','pastebin.com/u/','foursquare.com/','roblox.com/user.aspx?username=','gumroad.com/','wattpad.com/user/','canva.com/','creativemarket.com/','trakt.tv/users/','buzzfeed.com/','houzz.com/user/','blip.fm/','wikipedia.org/wiki/User:','news.ycombinator.com/user?id=','deviantart.com/','codementor.io/','reverbnation.com/','designspiration.net/','bandcamp.com/','colourlovers.com/love/', 'stackoverflow.com/users/', 'mixcloud.com/', 'bandcamp.com/', 'about.me/', 'angel.co/', 'producthunt.com/', 'kongregate.com/accounts/', 'newgrounds.com/', 'badoo.com/en/', 'okcupid.com/profile/', 'match.com/', 'plentyoffish.com/', 'tinder.com/', 'meetup.com/members/', 'kiva.org/lender/', 'venmo.com/', 'cash.app/', 'squareup.com/', 'stripe.com/', 'payoneer.com/', 'onlyfans.com/', 'xhamster.com/users/', 'pornhub.com/users/', 'xvideos.com/profiles/', 'redtube.com/', 'youporn.com/', 'tube8.com/', 'xnxx.com/', 'chaturbate.com/', 'cams.com/', 'cam4.com/', 'livejasmin.com/', 'streamate.com/', 'bongacams.com/', 'myfreecams.com/']

# Banner
def banner():
    GREEN(r'''
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

def check_username(site, username):
    url = f"https://{site}{username}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200 and username in response.text:
            YELLOW(f"{' '.join(site.split('.')[0].split('-')).title()}")
            GREEN(f"POSITIVE MATCH: - username detected in URL.")
            GREEN(f"\033[94m{url}\033[0m")
            return True
    except requests.exceptions.RequestException:
        pass
    return False

def search(username: str, max_threads=10):
    GREEN(f"[+] Searching for username: {username}")
    found_count = 0
    total_sites = len(WEBSITES)
    
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        results = executor.map(lambda site: check_username(site, username), WEBSITES)
    
    found_count = sum(results)
    GREEN(f"[FINISHED] {found_count} matches found out of {total_sites} websites.")

def main():
    banner()
    username = input("{+} Enter username: ")
    search(username)

if __name__ == "__main__":
    main()
