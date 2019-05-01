Onegin daily
============
Twitter Bot in Python
---------------------

See here: https://twitter.com/onegin_daily

Once upon a time the famous Russian poet Pushkin wrote his famous 
poem ["Eugene Onegin"](https://en.wikipedia.org/wiki/Eugene_Onegin).

Much later, just for fun, I wrote a trivial twitter bot,
which the only purpose was to publish one fourteen-line stanza
of that poem a day. Continuously. Forever. When it finishes the
entire poem, it waits for three weeks and starts again.

The bot is so old that initially it used `python 2.6`.

How it works
------------
There are carefully prepared tweets for each day in the `/tweets` 
folder. Each file contains all tweets for one day.

A source file looks like this:

    Печально подносить лекарство,
    Вздыхать и думать про себя:
    Когда же черт возьмет тебя!"\\
    Какое низкое коварство
    Полуживого забавлять,
    Ему подушки поправлять,\\
    Его пример другим наука;
    Но, боже мой, какая скука
    С больным сидеть и день и ночь,
    Не отходя ни шагу прочь!\\
    "Мой дядя самых честных правил,
    Когда не в шутку занемог,
    Он уважать себя заставил
    И лучше выдумать не мог.\\
    Г Л А В А   П Е Р В А Я
       И жить торопится и чувствовать спешит.
                          Кн. Вяземский.
    I

The bot takes a tweet file and splits it using the `\\` as a separator.
Each split is a single tweet. Therefore this will be tweeted first:

    Печально подносить лекарство,
    Вздыхать и думать про себя:
    Когда же черт возьмет тебя!"

And the "header" is the last one:
    
    Г Л А В А   П Е Р В А Я
       И жить торопится и чувствовать спешит.
                          Кн. Вяземский.
    I
    
In one's twitter feed it will become a well separated stanza:

    Г Л А В А   П Е Р В А Я
       И жить торопится и чувствовать спешит.
                          Кн. Вяземский.
    I

    "Мой дядя самых честных правил,
    Когда не в шутку занемог,
    Он уважать себя заставил
    И лучше выдумать не мог.
    
    Его пример другим наука;
    Но, боже мой, какая скука
    С больным сидеть и день и ночь,
    Не отходя ни шагу прочь!
    
    Какое низкое коварство
    Полуживого забавлять,
    Ему подушки поправлять,
    
    Печально подносить лекарство,
    Вздыхать и думать про себя:
    Когда же черт возьмет тебя!"
    

There is a counter `current_pos` which stores the state of the bot. 
Initially it is equal to zero. I.e. on the first day, the bot takes the 
file number zero from the `/tweets` folder, and publishes it. 
After a successful tweet the current position is incremented. 
The next day the bot will take the next tweet. On the `n`-th day the bot 
will take the `n`-th file, as it is stated in the `current_pos`. 
But if one day the bot is unable to tweet
for some reason, the `current_pos` remains the same, and as soon as the
bot is back to live, it continues from where it has stopped.

Contents of the bot
-------------------
* the bot itself: `onegin_paste_bot.py`;
* a set of tweets, with 120 characters per tweet limit;
* the source text of `Eugene Onegin`, and a cutter which produces
  all those tweets (`chopper.py`). Some tricky places (like *Girls'
  song*) were processed manually;
* primitive statistics: followers count (`stat.py`)
* the script to remove all the tweets for the account 
  (`remove_all_tweets.py`)
