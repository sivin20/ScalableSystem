FROM python:3.11
ADD ./ .
RUN pip3 install scikit-learn fastapi
RUN pip3 install uvicorn
EXPOSE 8000
CMD uvicorn main:app