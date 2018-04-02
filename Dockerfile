FROM frolvlad/alpine-python2
COPY . /root/bot
WORKDIR /root/bot
RUN pip install -r requirements.txt
VOLUME /root/bot/downloads
CMD python init.py