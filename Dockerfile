FROM redhat/ubi8
RUN yum install python3 -y
RUN pip3 install flask
COPY p1.py /p1.py
CMD ["python3","/p1.py"]
