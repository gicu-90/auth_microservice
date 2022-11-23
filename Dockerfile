FROM python:3.8
COPY . /prj/drfapp
RUN pip3 install -r /prj/drfapp/config/requirements.txt
CMD [ "gunicorn", "--config", \
    "/prj/drfapp/config/gunicorn.py", \
    "core.wsgi" \
]

ENV HOME=/prj/drfapp
ENV APP_HOME=/prj/drfapp/source
WORKDIR $APP_HOME