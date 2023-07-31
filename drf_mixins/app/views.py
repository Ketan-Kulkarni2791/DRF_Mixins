# GenericAPIView and ModelMiixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (ListModelMixin, CreateModelMixin, RetrieveModelMixin,
UpdateModelMixin)


class StudentAPIIstCreate(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    
    
class StudentAPIRetrieveUpdate(GenericAPIView, RetrieveModelMixin, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    
    
    
    
    
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
