import requests
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Project
from .pagination import PageNumberPagination
from .schemas import RapidAPIResponse
from .serializers import ProjectSerializer


class ProjectListViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.select_related("author").all()
    pagination_class = PageNumberPagination
    http_method_names = ["get", "post", "put", "patch"]


class WordsMeaningAPI(APIView):
    def __rapid_api(self, word: str) -> RapidAPIResponse:
        url = f"https://wordsapiv1.p.rapidapi.com/words/{word}"

        headers = {
            "x-rapidapi-key": settings.RAPID_API_KEY,
            "x-rapidapi-host": "wordsapiv1.p.rapidapi.com",
        }

        try:
            response = requests.get(url, headers=headers)

            return RapidAPIResponse(**response.json())
        except requests.RequestException:
            return RapidAPIResponse(
                word=word, results=[], syllables={}, pronunciation={}, frequency=0.0
            )

    def get(self, request, word: str) -> Response:
        response = self.__rapid_api(word)

        return Response(response.as_dict())
