# maintenance-mode
A simple "maintenance mode" webpage, for when you're working on the real one. Powered by Flask.

If you have a website, sometimes you need to work on it. Fix it up. Maybe it's gone down on its own. This is a simple flask app to show a maintenance page while you're working.

There are lots of other ways to do this. You can do something like this in just NGINX, for example. I wrote this because it was useful to me in a situation where I had administrative control of the website itself, with its attendant supervisor/gunicorn processes, but not box-wide admin access. So no messing with NGINX configs without bothering the admin.

As it exists here in Github, this is a completely unbranded, generic maintenance page, with a nice panic-inducing red background. You'll want to update a few things, at least. At a minimum, edit ``maintenance.py`` and update the variables that govern the site name, logo, and colors. For more extensive customization, edit the template file directly.

To run:

    gunicorn maintenance:app
    
Happy maintaining!
