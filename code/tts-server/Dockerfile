FROM dustynv/l4t-pytorch:r36.2.0

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY app.py app.py

VOLUME /models

ENV HF_HOME=/models

CMD ["fastapi", "run", "app.py"]
