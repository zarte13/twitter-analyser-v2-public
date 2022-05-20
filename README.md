<h1>New Twitter Analyze</h1>

<p>This script gets real time Twitter's data using <b>Tweepy</b> library and analyze them to do sentiment analysis using <b>Textblob</b>.</p>

<h2>Description: </h2>
<ul>
  <li>Tweets is the function to interact with the twitter API v2</li>
  <li>Multiple is the function that accumulate data over a given timeframe (max 7 days, twitter limitation for none academic account</li>
  <li>Sentiment V1 is OBSELETE, uses old version and twitter API v1</li>
  <li>Sentiment V2 is made with textblob and simple sentiment analysis</li>
  <li>Sentiment V3 is made with a pre-trained model for tweet sentiment based roBERTa</li>
  <li>Appli simple uses data from Sentiment V3 to get an average daily sentiment using a simple average</li>
</ul>

<h2>References: </h2>
<ul>
  <li><a href="https://www.tweepy.org/">Tweepy</a></li>
  <li><a href="https://textblob.readthedocs.io/en/dev/">Textblob</a></li>
</ul>
