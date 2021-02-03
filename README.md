<h1> Sonogram Documentation </h1>
This is the documentation for Sonogram: an open-source webapp for sending 
sonograms to your friends. A sonogram is a robocall that
reads your friend the lyrics of a song on the phone with a follow-up text. 


<h3>Installation </h3>
You can clone the repository via the command line: <br>
<code>git clone https://github.com/calthoff/sonogram.git </code>

<h3>Dependencies </h3>
To use Sonogram, first install its dependencies using pip freeze:<br>
<code>pip freeze requirements.txt </code>

<h3>Environmental Variables </h3>
In web_app.py you need to set the following variables with your information from your Vonage account. You can
get this information by registering for an account on https://developer.nexmo.com/<br><br>
<code>
APPLICATION_ID = 'Your Vonage application ID.' <br>
PRIVATE_KEY = 'Filepath to your Vonage private key.' <br>
VONAGE_API_KEY = "Your Vonage API key." <br>
VONAGE_API_SECRET = "Your Vonage API secret." <br>
VONAGE_BRAND_NAME = "Your Vonage Brand Name" <br>
</code>
<br> In production, you should set and get them from environmental variables. 

<h3> Usage </h3>
You can send a sonogram either by using the Sonogram API or by using 
the web app UI. <br><br>
<h5> API </h5>
Here is how to send a songogram via API <br>
1. Run webapp.py on your local machine. <br>
2. Send a get request to http://127.0.0.1:5000/API/1.0.0/sonogram
<br><b>Required parameters:</b><br>
<i>name</i>: The name of the person sending the sonogram <br>
<i>artist_fname</i>: The first name of the musician for the song you are sending. <br>
<i>artist_lname</i>: The last name of the musician for the song you are sending. <br>
<i>song_name</i>: The name of the song you are sending. <br>
<i>number</i>: The number you are sending a sonogram to.<br>
<br>
<b>Example:</b> http://127.0.0.1:5000/API/1.0.0/songogram?name=Cory+Althoff&artist_fname=Kanye+&artist_lname=West&song_name=Stronger&number=16507763446
   
<h5> Web App </h5>

Or:
1. Run webapp.py on your local machine. <br>
2. Navigate to http://127.0.0.1:5000 in your web browser and use the UI. 

<h3> License </h3>
This library is released under the MIT License.
 