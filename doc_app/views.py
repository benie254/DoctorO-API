from django.shortcuts import render
from django.template.loader import render_to_string

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from doc_app.serializers import ContactSerializer

from decouple import config

import sendgrid 
from sendgrid.helpers.mail import *

from datetime import date

from drf_yasg.utils import swagger_auto_schema


# Create your views here.
def Landing(request):
    title = 'welcome'
    return render(request,'landing.html',{"title":title,})

@permission_classes([AllowAny,])
class Contacts(APIView):
    @swagger_auto_schema(request_body=ContactSerializer)
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            message = serializer.validated_data['message']
            serializer.save()
            sg = sendgrid.SendGridAPIClient(api_key=config('SENDGRID_API_KEY'))
            year = date.today().year
            msg = render_to_string('email/msg-new.html', {
                'name': name,
                'email': email,
                'message': message,
                'year': year,
            })
            msg2 = render_to_string('email/msg-sent.html', {
                'name': name,
                'message': message,
                'year': year,
            })
            message = Mail(
                from_email = Email("davinci.monalissa@gmail.com"),
                to_emails = "fowiti@africaonline.co.ke",
                subject = "New Message",
                html_content = msg
            )
            try:
                sendgrid_client = sendgrid.SendGridAPIClient(config('SENDGRID_API_KEY'))
                response = sendgrid_client.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e)
            message2 = Mail(
                from_email = Email("davinci.monalissa@gmail.com"),
                to_emails = email,
                subject = "Message Delivered",
                html_content = msg2
            )
            try:
                sendgrid_client = sendgrid.SendGridAPIClient(config('SENDGRID_API_KEY'))
                response = sendgrid_client.send(message2)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e)
            status_code = status.HTTP_201_CREATED
            response = {
                'success' : 'True',
                'status code' : status_code,
                'message': 'Message sent successfully',
                }
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)