FROM python:3.6.1
COPY bin/_util requirements.txt *.py dev/main.sh /main_build/
RUN bash /main_build/main.sh
CMD python main.py
