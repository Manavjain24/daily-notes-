today we would be talking about dockerfiles 
so the use of docker id docker can be use to build images automatically from the instructions from dockerfile.
q1)why is docker being used in the professional world ?
a - so docker is being used to store the the information in the container 
q2) why does it use images then ?
a -- so docker can be used to store the blueprint of the information in the form of image and the container is being used to running instance of the image 
so here are some common command lines being used in the application 
Instruction	Description
ADD	Add local or remote files and directories.
ARG	Use build-time variables.
CMD	Specify default commands.
COPY	Copy files and directories.
ENTRYPOINT	Specify default executable.
ENV	Set environment variables.
EXPOSE	Describe which ports your application is listening on.
FROM	Create a new build stage from a base image.
HEALTHCHECK	Check a container's health on startup.
LABEL	Add metadata to an image.
MAINTAINER	Specify the author of an image.
ONBUILD	Specify instructions for when the image is used in a build.
RUN	Execute build commands.
SHELL	Set the default shell of an image.
STOPSIGNAL	Specify the system call signal for exiting a container.
USER	Set user and group ID.
VOLUME	Create volume mounts.
WORKDIR	Change working directory.

whenver there is # in docker file in line except in the begginnig  that would be treated as an argument 
-- so thing with docker file is that it follows everything in order in the file 
-- parser directives are placed at the top of every document in this 
the main 3 tags of parser directives such as escape , syntax and check are being used \
-- the syntax parser directive is being used to declare the version being used of the docker file example -- docker/dockerfile:1 is used to pull out the latest version of the 
-- escape parser is being used to make sure that correct escape character is being used 
example -- #escape = \
-- check is being used to make sure that dockerfile build checks example --#check = error = true 

Enviornment replacement 
-- enviornment variables can also be used in certain instruction as variables to be interpreted by docker 
-- enviornment variables like name of the variable is being specified in the braces like ${vaiable_name}
some of the bash commands are as follows 
${variable:-word} indicates that if variable is set and non-empty then the result will be that value. If variable is unset or empty then word will be the result.
${variable-word} indicates that if variable is set (even if empty) then the result will be that value. If variable is unset then word will be the result.
${variable:+word} indicates that if variable is set and non-empty then word will be the result, otherwise the result is the empty string.
${variable+word} indicates that if variable is set (even if empty) then word will be the result, otherwise the result is the empty string.

some of the parser directive instruction are as follows 
ADD
COPY
ENV
EXPOSE
FROM
LABEL
STOPSIGNAL
USER
VOLUME
WORKDIR
ONBUILD (when combined with one of the supported instructions above)
