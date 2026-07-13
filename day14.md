what are image layers?
before that we should recall that images are used to store information that is the blueprint of the system that would be occuring, so image layers are basically the changes are being made 
so image layers are being used to store information layerwise for example 
The first layer adds basic commands and a package manager, such as apt.
The second layer installs a Python runtime and pip for dependency management.
The third layer copies in an application’s specific requirements.txt file.
The fourth layer installs that application’s specific dependencies.
The fifth layer copies in the actual source code of the application.

why is this benificial ?
a -- because it allows layers to be reused within images 

so now we would be studying build optimisation for docker 
1) slim the size of the image as less as possible 
2) multi stage tools 

so here is the docker compose section 
so why is it used ?
ans -- docker compose is being used to run multiple stack configuration application together.

what are benifits of it ?
ans -- 


how compose file works ??
a -- compose file uses the compose.yaml file to configure the application file 

