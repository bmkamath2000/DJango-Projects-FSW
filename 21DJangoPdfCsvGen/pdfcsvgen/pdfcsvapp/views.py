from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from .models import Book
from django.shortcuts import redirect, render
from .forms import BookForm
import csv  

def home(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    # Redirect to PDF generation after adding a book
            return redirect('home')  
    else:
        form = BookForm()
    return render(request, 'pdfcsvapp/create_book_record.html', 
                  {'form': form})
 
def generate_pdf(request):
    response = FileResponse(generate_pdf_file(), 
                            as_attachment=True, 
                            filename='book_catalog.pdf')
    return response
 
 
def generate_pdf_file():
    from io import BytesIO
 
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
 
    # Create a PDF document
    books = Book.objects.all()
    p.drawString(100, 750, "Book Catalog")
    i = 1
    y = 700
    for book in books:
        p.drawString(100, y, "(%s)"% i)
        p.drawString(100, y - 20, f"Title: {book.title}")
        p.drawString(100, y - 40, f"Author: {book.author}")
        p.drawString(100, y - 60, f"Year: {book.publication_year}")
        y -= 80
        i = i + 1
 
    p.showPage()
    p.save()
 
    buffer.seek(0)
    return buffer

def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="books.csv"'  
    books = Book.objects.all()  
    writer = csv.writer(response)  
    for book in books:  
        writer.writerow([book.title,book.author,book.publication_year])  
    return response 