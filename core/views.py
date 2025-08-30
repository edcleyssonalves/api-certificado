from rest_framework import views, response, status
from .tasks import generate_certificate, send_notification, update_student


class CertificateView(views.APIView):

    def post(self, request):
        data = request.data

        generate_certificate.delay(data)
        send_notification.delay(data)
        update_student.delay(data)

        return response.Response(
            data={
                'status': 'ok',
                'message': 'Certificado gerado e enviado com sucesso.',
                'data': data,
            },
            status=status.HTTP_201_CREATED,
        )