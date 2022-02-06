FROM centos
RUN yum install python3 -y
RUN pip3 install sklearn
RUN pip3 install pandas
COPY task4.py /task4.py
COPY salaryData.csv /salaryData.csv
ENTRYPOINT ["python3","task4.py"]
