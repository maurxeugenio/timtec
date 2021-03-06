# -*- coding: utf-8 -*-
from braces.views import LoginRequiredMixin
from core.models import Course
from course_material.forms import FileForm
from course_material.serializers import CourseMaterialSerializer, FilesSerializer, CourseMaterialFileHideSerialilizer
from course_material.models import CourseMaterial, File as CourseMaterialFile
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from rest_framework import viewsets, filters
from administration.views import AdminMixin


class CourseMaterialView(LoginRequiredMixin, DetailView):
    model = CourseMaterial
    context_object_name = 'course_material'
    template_name = 'course-material.html'
    slug_field = 'course__slug'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CourseMaterialView, self).get_context_data(**kwargs)
        self.course = get_object_or_404(Course, slug=self.kwargs['slug'])
        context['course'] = self.course
        return context


class FileUploadView(LoginRequiredMixin, CreateView):
    form_class = FileForm
    success_url = '/'
    template_name = 'base.html'

    def form_valid(self, form):
        super(FileUploadView, self).form_valid(form)
        return HttpResponse()


class CourseMaterialAdminView(AdminMixin, DetailView):
    model = CourseMaterial
    context_object_name = 'course_material'

    def get_object(self, queryset=None):
        course_id = self.kwargs.get('pk', None)
        return get_object_or_404(CourseMaterial, course__id=course_id)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CourseMaterialAdminView, self).get_context_data(**kwargs)
        self.course = get_object_or_404(Course, id=self.kwargs['pk'])
        context['course'] = self.course
        return context


class CourseMaterialViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    model = CourseMaterial
    queryset = CourseMaterial.objects.all()
    serializer_class = CourseMaterialSerializer
    lookup_field = 'course'
    filter_fields = ('course__id',)
    filter_backends = (filters.DjangoFilterBackend,)

    def update(self, request, **kwargs):
        return super(CourseMaterialViewSet, self).update(request, **kwargs)


# class CourseMaterialFileViewSet(LoginRequiredMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet, mixins.UpdateModelMixin):
class CourseMaterialFileViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = CourseMaterialFile.objects.all()
    model = CourseMaterialFile
    serializer_class = CourseMaterialFileHideSerialilizer
    lookup_field = 'id'
    filter_fields = ('id',)
    filter_backends = (filters.DjangoFilterBackend,)
