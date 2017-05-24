FROM python:3.6.1
COPY source_script/util ap/requirements.txt dev/main.sh /main_build/
COPY ap/*.py /usr/src/app/
RUN bash /main_build/main.sh
WORKDIR /usr/src/app
CMD python main.py
