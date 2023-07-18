FROM python:3.8.10
COPY requirement.txt requirement.txt
COPY rajeev.py rajeev.py
RUN pip3 install -r requirement.txt
CMD ["python", "rajeev.py"]
