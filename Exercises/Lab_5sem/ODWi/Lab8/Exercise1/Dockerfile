FROM ubuntu
RUN apt-get update 
RUN apt-get install build-essential -y
COPY . .
RUN make all
CMD bash
#I terminal:
    #docker build -t code .
    #docker run -it code . #-it for at komme ind i containeren
    #ls
    #./code1
    #exit

#Den manuelle måde at gøre tingene på
#COPY /code1.c C:\GitHub\Lab\5sem\ODWi\Lab8\multitasking\code1.c 
#COPY ./ /code1.c/
#COPY ./ /code2.c/
#COPY ./ /code3.c/
#COPY ./ /code4.c/
#COPY ./ /code5.c/
#RUN gcc -o code1.c -lpthread code1.c
#RUN gcc -o filename -lpthread code.c
#RUN gcc -o filename code.c -lpthread