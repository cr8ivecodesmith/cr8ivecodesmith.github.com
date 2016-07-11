Title: the way of the pelican and the order of silly walks
Date: 2013-05-25 18:00
Category: code
Status: published


Once there was boy who wrote magnificent stories about technology and the
internets. He talked about tales of discoveries and adventures, of code and
sorcery, of... *well you get the point*.

Let me tell you his story.


## the art of blogging

For many months he poured all of his energy in an ancient art called 
"blogging".

He learned about the arcane languages called "HTML", "CSS", and 
"Javascript" that is used to invoke the necessary spells to put up a 
"website" that runs inside these puny looking contraptions called 
"servers".

And so he wrote one webpage after another. Days went by like a puff of 
smoke. He wrote with so much glee it seemed like madness.

One day, while he was out for a walk, he discovered a magical piece of 
software called a "CMS". He spent quite a while researching and learning 
about it. He learned that in order to wield it one must setup a "Database" 
among many things.

"This could really improve my blogging techniques!", he thought.

So off with the old and into the new! He started using the "CMS" and got
absorbed in its power and extravagance.


## complexity

Many months passed by and his website grew in popularity. Traffic surged 
and things appear to have taken a new direction.

He became focused on the black arts of getting more mailing list 
subscribers, selling affiliate products, gaining more social network 
followers. Even the topics he chose to write about have become focused 
around these matters.

He also casted one "plugin" after another as the CMS permits its wielder to
extend its power with such spells. All of which are for vanity's sake.

Eventually he spent more time configuring than writing.


## losing purpose

As he continues down this new path, the boy started becoming weary. 
Inspite of the lights, glamour and all things shiny, he felt empty. Lost.

"Everything appears to be going well but it all feels wrong somehow...", he
thought.

For a brief moment (about 2 seconds) he remembered the days of old. With 
only a simple parchment he calls a "text editor", he wrote stories of his 
discoveries and adventures and how he would go about it for many hours. 
It was the good times indeed. With nothing but the innocence and the 
passion of sharing.

"I've become lost.", he mumbled.

And so the very next day the boy set off to a journey to find himself once 
more.


## the order of silly walks

He travelled for many days. He went from one village to the next. He 
trekked on great plains, majestic mountains, and myterious forests.

One day while he was out for a drink along a stream, he saw a group of 
merry men doing some sort of outlandish dancing.

Curious about what's going on, he cautiously approached one of them.

"What do you call this silly dancing, sir?", the boy asked.

"Dancing?! Preposterous! We are channeling our energies to wield a 
powerful, yet cleverly simple, software called the Pelican.", the man 
replied.

Later he learned that the group was called the Order of 
[Silly Walks](http://www.youtube.com/watch?v=IqhlQfXUk7w). They too are 
bloggers like him and gained a cult following of audience. But they 
appeared different somehow. They looked happy, fulfilled, simple to the 
core.


## a <del>not so</del> new path

"I must know their secret!", he thought.

Mustering his strength, he asked the man once more...

"You need not ask young man. You appear to have to lost your way and so we 
shall show you the path back your self. We shall teach you the way of the 
Pelican!", said the man.


## the way of the pelican

"In this training you shall learn to create good old static websites and 
host it on Github."  

"First things first, I shall assume that you have a Github account, 
git, python, a terminal, and your running Ubuntu. Otherwise, move on and 
learn them some place else then come back to me."  

"With those things prepared let's begin your training."  


- Fire up your terminal and install VirtualEnv + Virtualenvwrapper  

~~~~~
$ sudo apt-get install -V python-setuptools python-dev
$ sudo easy_install --upgrade pip
$ sudo pip install virtualenv
$ sudo pip install virtualenvwrapper
~~~~~

- Create a virtualenv directory and set your projects directory  

~~~~~
$ mkdir ~/.virtualenvs
$ mkdir ~/Projects
~~~~~

- Update ~/.bashrc

"From here on I shall be using Vim for text editing, but you're free to use 
your favorite text editor.", the man reminded the boy.  

~~~~~
$ vim ~/.bashrc
~~~~~

"Add the following text at the end of the file."  

~~~~~
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Projects
source /usr/local/bin/virtualenvwrapper.sh
~~~~~

- Create a Virtual Environment  

~~~~~
$ mkvirtualenv pelican_blog
~~~~~

"Then your prompt will turn into something like this..."  

~~~~~
(pelican_blog) $ 
~~~~~

- Go to your Github account and create a new repo for your blog and name 
  it:  

~~~~~
*your_username*.github.com  
~~~~~

"Using your *username* is important here so that github will know that 
you're trying to create a Github page.", the man warned.  


- Clone it to your local directory  

~~~~~
(pelican_blog) $ git clone git@github.com:*username*/*your_username*.github.com.git ~/Projects/my_blog
~~~~~

- Go to your working directory  

~~~~~
(pelican_blog) $ cd ~/Projects/my_blog
(pelican_blog)my_blog $ 
~~~~~

- Install pelican + markdown  

~~~~~
(pelican_blog)my_blog $ pip install pelican
(pelican_blog)my_blog $ pip install Markdown
~~~~~

- Create a post in markdown  

~~~~~
(pelican_blog)my_blog $ mkdir .content
(pelican_blog)my_blog $ vim .content/my_first_blogpost.md
~~~~~

"You must have the following spell at the top of your file in order for 
Pelican to recognize your post."

~~~~~
Title: hello world
Date: 2013-05-25 18:00
Category: code
Tags: pelican, python
Slug: the-way-of-the-pelican
Author: juan tamad

"Somewhere below that you may begin writing your story."

Hello world!
~~~~~

- Create a settings.py

~~~~~
(pelican_blog)my_blog $ vim settings.py
~~~~~

~~~~~
from __future__ import unicode_literals

AUTHOR = 'juan tamad'
SITENAME = 'the misadventures of juan tamad'
SITEURL = 'http://juantamad.ph'
DEFAULT_DATE_FORMAT = '%A, %B %d, %Y'

GITHUB_URL = 'https://github.com/*username*/*your_username*.github.com'

TIMEZONE = 'Asia/Manila'
DEFAULT_PAGINATION = 1
~~~~~


"More settings can be found [here](http://docs.getpelican.com/en/3.1.1/settings.html)."


- Generate the HTML files

~~~~~
SYNTAX:
pelican <input_dir> -o <output_dir> -s <settings_file.py>
~~~~~

~~~~~
(pelican_blog)my_blog $ pelican .content -o . -s settings.py
~~~~~

- Check it out

~~~~~
(pelican_blog)my_blog $ firefox index.html
~~~~~

- Push your changes to Github  

~~~~~
(pelican_blog)my_blog $ git add -A
(pelican_blog)my_blog $ git commit -m "The blog has begun!"
(pelican_blog)my_blog $ git push origin master
~~~~~

- Visit your new shiny site  

~~~~~
(pelican_blog)my_blog $ firefox http://*your_username*.github.com
~~~~~

## and finally

Several months later the boy has finished his training and with his new 
found enlightenment, he went back home happier for once more the focus of 
his blog is about creating wonderful content. The days of joy went on for 
many years... until further notice.
