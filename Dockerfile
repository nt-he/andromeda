FROM python/python3.9

RUN useradd --disable-password server
COPY . /usr/bin/scripts/Andromeda

COPY andromeda_web.service /usr/lib/systemd/system/andromeda_web.service

RUN systemctl daemon-reload
RUN systemctl enable andromeda_web.service
RUN apt install -y python3 python3-pip python3-dev python3-venv python3-wheel
RUN pip3 install --upgrade pip
RUN pip3 install pipenv
WORKDIR /usr/bin/scripts/Andromeda
USER server
RUN pipenv install

ENTRYPOINT [ "/usr/bin/env", "pipenv", "run", "python", "bot.py"]

