FROM public.ecr.aws/lambda/python:3.10 as base

COPY . ./

RUN pip install -r requirements.txt

ADD api.py ${LAMBDA_TASK_ROOT}

CMD ["api.handler"]