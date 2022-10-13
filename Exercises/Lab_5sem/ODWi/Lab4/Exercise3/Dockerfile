FROM ubuntu 
COPY ./ /home/
RUN apt-get update 
RUN apt install python3 -y 
RUN apt install Flask -y
CMD python3 /home/hello2.py

#FROM python3, pip3, flask, alpine
#RUN install: pip3