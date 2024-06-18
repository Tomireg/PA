URL on render: https://pa-3so9.onrender.com 
Use the url provided by render to access the site
Challenges: 
Render.com gives a warning that it treats the generated animation as garbage and it gets deleted. I could not work around this but thanks to the animation being generated already while testing locally, it is working. I left the problematic code in the app because it’s working on render despite the warning and I wanted to show how I generated the gif. This web app is a portfolio. I made a game page to showcase some python skills. The projects page contains my previous works. I removed the login forms because it made no sense in the context of a portfolio page. I added other ways to use the post method instead. I wanted to create a proper contact page with email composing and sending however it required a domain, which I don’t have, and mailtrap, which I tried to use, would not work without one so I had to remove the code. I also tried to make a more complex classic snake game, written with python, first but render didn’t like it so I had to remove that code as well. These took a bit of time that I could have used to write code that works, but I learned a lot from these endeavors and I can use that new knowledge in upcoming projects so I don’t regret doing it.

How to deploy on Render.com:
Environment tab on render:
Set the python version to 3.12.2
PYTHON_VERSION 3.12.2

Settings tab on render:
Set the region to Frankfurt.
Use github repository: https://github.com/Tomireg/PA
Set the branch to main.
Set the root directory to flask.
Build command: pip install -r requirements.txt
Contents of requirements.txt:
blinker==1.7.0
click==8.1.7
colorama==0.4.6
Flask==3.0.2
gunicorn==21.2.0
itsdangerous==2.1.2
Jinja2==3.1.3
MarkupSafe==2.1.5
packaging==24.0
six==1.16.0
Werkzeug==3.0.2
numpy==1.26.4
matplotlib==3.9.0
Start command: gunicorn app:app
Auto-deploy: yes
Deploy hook: https://api.render.com/deploy/srv-co8hp2ol5elc738v33r0?key=1v2K2tkFKjA

Sources:
https://favicon.io/
https://www.techwithtim.net/tutorials/flask/http-methods-get-post
https://www.geeksforgeeks.org/python-using-for-loop-in-flask/
https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
https://www.geeksforgeeks.org/using-matplotlib-for-animations/
https://matplotlib.org/stable/users/explain/animations/animations.html
https://matplotlib.org/stable/tutorials/pyplot.html


