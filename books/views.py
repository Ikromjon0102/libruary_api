from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status': f'Returned {len(books)} books',
            'books' : serializer_data,
        }
        return Response(data)


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailApiView(APIView):

    def get(self,request, pk):
        try:
            book = get_object_or_404(Book,id=pk)
            serializer_book = BookSerializer(book).data
            data = {
                'status' : "Success",
                'book' : serializer_book
            }
            return Response(data)
        except Exception:
            data = {
                'status':'does not exists',
                'messaga':'Book is not found',
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
# class BookDeleteApiview(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiview(APIView):

    def get(self,request, pk):

        book = get_object_or_404(Book,id=pk)
        book.delete()
        # del serializer_book
        data = {
            'status' : True,
            'book' : 'Successfully deleted'
        }
        return Response(data)


# class BookUpdateApiview(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateApiview(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id = pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()

        return Response({
                'status' : True,
                'message': f"Book {book_saved} update successfully"
            }
        )


# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': f'Books are saved to database',
                'books' : data
            }
            return Response(data)
        # else:
        #     return Response({
        #         'status':'Request is not full',
        #         'message':'Your head is place'
        #     }, status=status.HTTP_400_BAD_REQUEST())



class BookListCreateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListCreateNewApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer




# @api_view(['GET'])
# def book_list_view(request,*args, **kwargs):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)

