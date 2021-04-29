from fpdf import FPDF




""" FLASK APP
    from flask import Flask, redirect, url_for, render_template, send_file

    app = Flask(__name__)
    app.secret_key = "hello"

    @app.route('/download/')
    def download_file():    
        print('test')
        p = "plik.pdf"
        return send_file(p,as_attachment=True)

    if __name__ == "__main__":
        app.run(debug=True)
"""


"""
class PDF(FPDF):
    def header(self):
        #logo
        self.image('university.png', 10, 8, 25)
        #font
        self.set_font('helvetica', 'B', 20)
        #Title
        self.cell(0,10, 'Title', border=False, ln=True, align='C')
        #line break 
        self.ln(20) 
    
    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 10)
        self.cell(0,10, f'Page {self.page_no()}/{{nb}}', align='C')
"""

# create PDF object
pdf = FPDF('P', 'mm', 'A4')


# ustawia auto przechodzenie do nastepnej strony
pdf.set_auto_page_break(auto=True, margin = 15) # margin -> na koncu strony margin

"""
Layout ('P', 'L')
Unit ('mm', 'cm', 'in')
formats (A3, A4 (default), A5, Letter, Legal, Custom - (100,150) (width, hight) )
align = 'C'  - > Center

"""



#create page
pdf.add_page()

#specify font

pdf.set_font('helvetica', '', 16)
# pdf.set_text_color(220,50,50)
# add text
# w = width
# h = height
# , ln = True - cursor to next line
# border = True


pdf.image('profilowe.jpg', 20, 10, 40) # szerokosc , wysok, wielkosc

pdf.set_font('helvetica', 'B', 18)
pdf.cell(0,10, '- CV -', border=False, ln=True, align='C')
pdf.set_font('helvetica', '', 16)
pdf.cell(0,8, 'IMIE NAZWISKO', border=False, ln=True, align='C')
pdf.cell(0,8, 'E-mail: mail@gmail.com', border=False, ln=True, align='C')
pdf.cell(0,8, 'Phone number: 123-456-789', border=False, ln=True, align='C')
pdf.cell(0,15, 'Birth date: 01.01.1990', border=False, ln=True, align='C')
pdf.cell(0,0, 'City: London', border=False, ln=True, align='C')
pdf.cell(0,10, '', border=False, ln=True, align='C')
pdf.cell(0,10, 'EXPERIENCE', border=False, ln=True, align='C')
pdf.cell(0,0, '', border=True, ln=True, align='C')
# Experience - 1'st company
pdf.cell(0,5, '', border=False, ln=True, align='C')
pdf.cell(0,8, '01.2019 - 09.2020', border=False, ln=True)
pdf.cell(0,8, 'Freght Forwarding Specialist | Company Name | Poland', border=False, ln=True)
pdf.cell(0,10, 'Description:', border=False, ln=True)
pdf.cell(0,8, '- example 1', border=False, ln=True)
pdf.cell(0,8, '- example 1', border=False, ln=True)
# Experience - 2'st company
pdf.cell(0,5, '', border=False, ln=True, align='C')
pdf.cell(0,8, '01.2019 - 09.2020', border=False, ln=True)
pdf.cell(0,8, 'Freght Forwarding Specialist | Company Name | Poland', border=False, ln=True)
pdf.cell(0,10, 'Description:', border=False, ln=True)
pdf.cell(0,8, '- example 1', border=False, ln=True)
pdf.cell(0,8, '- example 1', border=False, ln=True)

# Education
pdf.cell(0,10, 'EDUCATION', border=False, ln=True, align='C')
pdf.cell(0,0, '', border=True, ln=True, align='C')
pdf.cell(0,5, '', border=False, ln=True, align='C')
pdf.set_font('helvetica', 'B', 14)
pdf.cell(0,8, '01.2019 - 09.2020', border=False, ln=True)
pdf.set_font('helvetica', '', 16)
pdf.cell(0,8, 'Name of University | Subject', border=False, ln=True)
pdf.set_font('helvetica', 'B', 14)
pdf.cell(0,10, 'Description:', border=False, ln=True)
pdf.set_font('helvetica', '', 16)
pdf.cell(0,8, '- example 1', border=False, ln=True)
pdf.cell(0,8, '- example 1', border=False, ln=True)







try: 
    pdf.output('pdf_3.pdf')
except:
    print('Błąd: otwaty pdf')

