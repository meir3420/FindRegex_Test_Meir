# To build Docker run the following: docker build -t findregexapp .

FROM python
RUN mkdir c:\home\findregex
COPY findregex.py /home/findregex/findregex.py
COPY files_for_unittest/first.txt /home/findregex/first.txt
COPY files_for_unittest/second.txt /home/findregex/second.txt
CMD python /home/findregex/findregex.py -c /home/findregex/first.txt /home/findregex/second.txt [a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]
