from pickle import TRUE
from django.shortcuts import render
from django.http import FileResponse
import io 
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# Create your views here.

def test(request):
    return render(request, 'testttt/test.html')

def pdf(request):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
    text=c.beginText()
    text.setTextOrigin(inch,inch)
    text.setFont("Helvetica",14)
 
    lines=[
        "this is line 1",
        "this is line 2",
        "this is line 3",
    ]
    for i in lines:
        text.textLine(i)

    c.drawText(text)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf,as_attachment=True,filename='venue.pdf')


