from urllib.request import Request, urlopen
from vonage import Client, Voice, Sms
from bs4 import BeautifulSoup
import os

# In Production, these should come from environmental variables
VONAGE_API_KEY = "Your Vonage API key."
VONAGE_API_SECRET = "Your Vonage API secret. "
VONAGE_NUMBER = 'Your Vonage number'

APPLICATION_ID = 'Your  Vonage application ID.'
PRIVATE_KEY = os.join('Filepath to your Vonage private key.')

SCRAPE_SITE = 'http://www.songlyrics.com/{}-{}/{}-lyrics/'



def send_songogram(your_name, artist_first_name, artist_last_name, song_name, number_to_call):
    """ Function for sending a Sonogram.
    :param your_name: string containing the person sending the sonogram's name.
    :param artist_first_name: string containing the musician's first name.
    :param artist_last_name: string containing the musician's last name.
    :param song_name: string containing the song name.
    :param number_to_call: string of the telephone number to send a sonogram to.
    """
    lyrics = scrape_lyrics(artist_first_name, artist_last_name, song_name)
    make_call(number_to_call, lyrics, your_name)
    send_text(song_name, artist_first_name + ' ' + artist_last_name, number_to_call, your_name)


def scrape_lyrics(first_name, last_name, song_name,):
    """ Function for scraping lyrics from songlyrics.com
    :param first_name: string containing the musician's first name.
    :param last_name: string containing the musician's last name.
    :param song_name: string containing the song name.
    :return: string containing the song's lyrics.
    """
    req = Request(
        SCRAPE_SITE.format(first_name, last_name, song_name.replace(" ", "-")),
        headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    parser = "html.parser"
    soup = BeautifulSoup(html, parser)
    return soup.find("p", {"class": "songLyricsV14"}).text


def make_call(number_to_call, text, your_name):
    """ Function for sending a sonogram via phonecall using Vonage's API
    :param number_to_call: string containing the number to call.
    :param text: string containing the text to read during the call.
    :param your_name: string containing the name of the person sending a sonogram.
    """
    if len(text) > 1000:
        text = text[:1000]

    ncco = [
      {
        'action': 'talk',
        'voiceName': 'Joey',
        'text': 'This is a songogram from {} {}'.format(your_name, text)
      }
    ]

    client = Client(application_id=APPLICATION_ID, private_key=PRIVATE_KEY)
    voice = Voice(client)
    response = voice.create_call({
      'to': [{'type': 'phone', 'number': '{}'.format(number_to_call)}],
      'from': {'type': 'phone', 'number': VONAGE_NUMBER},
      'answer_url': ['https://example.com/answer'],
      'ncco': ncco
    })
    voice.send_speech(response['uuid'], text='Hello from songogram')


def send_text(song_name, artist, number_to_text, your_name):
    """ Function for sending a songogram text confirmation.
    :param song_name: string containing the song name.
    :param artist: string containing the artist's name.
    :param number_to_text: string containing the number to text.
    :param your_name: string containing the person sending the sonogram's name.
    """
    client = Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)
    sms = Sms(client)
    response_data = sms.send_message(
        {
            "from": VONAGE_NUMBER,
            "to": number_to_text,
            "text": "Hello! You are receiving a songogram of the song {} by {} from your friend {}".format(song_name, artist, your_name),
        }
    )

    if response_data["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {response_data['messages'][0]['error-text']}")






