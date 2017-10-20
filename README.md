# Brevet time calculator with Ajax

Reimplement the RUSA ACP controle time calculator with flask and ajax

## ACP controle times

That's "controle" with an 'e', because it's French, although "control"
is also accepted.  Controls are points where   
a rider must obtain proof of passage, and control[e] times are the
minimum and maximum times by which the rider must  
arrive at the location.   

The algorithm for calculating controle times is described at
https://rusa.org/octime_alg.html .  Additional background information
is in https://rusa.org/pages/rulesForRiders . The description is ambiguous,
but the examples help.  Part of finishing this project is clarifying
anything that is not clear about the requirements, and documenting it
clearly.  


## Usages
-  With a default controle specification file and a brevet overall time limits' list file OOB.
-  You can modify these files in <programme's folder>/data/ or you can assign a new directory by modifying the app.ini file.
-  Just type "make start" in the terminal, and it will be online.