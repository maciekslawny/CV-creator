from fpdf import FPDF
import random

def sort_data(input_data):
    personal = {
        'name': input_data[0][0],
        'surname': input_data[0][1],
        'email': input_data[0][2],
        'phone': input_data[0][3],
        'birthday': input_data[0][4],
        'city': input_data[0][5]
        }
    
    experiences = {}
    number = 1
    for experience in input_data[1]:
        experiences[f'company{number}'] = {
            'name': experience[0],
            'position': experience[1],
            'place': experience[2],
            'startdate': experience[3],
            'enddate': experience[4],
            'description': experience[5]
        }
        number = number + 1

    education = {}

    number = 1
    for university in input_data[2]:
        education[f'university{number}'] = {
            'name': university[0],
            'subject': university[1],
            'startdate': university[2],
            'enddate': university[3],
            'description': university[4],
        }
        number = number + 1


    
    
    output_data = {
        'personal': personal,
        'experiences': experiences,
        'education': education
        }    

    
        
    return output_data


def create_cv_pdf(input_data, image_name):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_auto_page_break(auto=True, margin = 15)
    pdf.add_page()
    pdf.set_font('helvetica', '', 16)
    pdf.image(f'uploads/{image_name}', 20, 10, 40)



    pdf.set_font('helvetica', 'B', 18)
    pdf.cell(0,10, '- CV -', border=False, ln=True, align='C')
    pdf.set_font('helvetica', '', 16)
    pdf.cell(0,8, f'{input_data["personal"]["name"]} {input_data["personal"]["surname"]}', border=False, ln=True, align='C')
    pdf.cell(0,8, f'E-mail: {input_data["personal"]["email"]}', border=False, ln=True, align='C')
    pdf.cell(0,8, f'Phone number: {input_data["personal"]["phone"]}', border=False, ln=True, align='C')
    pdf.cell(0,15, f'Birth date: {input_data["personal"]["birthday"]}', border=False, ln=True, align='C')
    pdf.cell(0,0, f'City: {input_data["personal"]["city"]}', border=False, ln=True, align='C')
    pdf.cell(0,10, '', border=False, ln=True, align='C')
    pdf.cell(0,10, 'EXPERIENCE', border=False, ln=True, align='C')
    pdf.cell(0,0, '', border=True, ln=True, align='C')


    for experience in input_data['experiences']:

        # Experience - 1'st company
        pdf.cell(0,5, '', border=False, ln=True, align='C')
        pdf.cell(0,8, f'{input_data["experiences"][experience]["startdate"]} - {input_data["experiences"][experience]["enddate"]}', border=False, ln=True)
        pdf.cell(0,8, f'{input_data["experiences"][experience]["position"]} | {input_data["experiences"][experience]["name"]} | {input_data["experiences"][experience]["place"]}', border=False, ln=True)
        pdf.cell(0,10, 'Description:', border=False, ln=True)
        pdf.cell(0,8, f'{input_data["experiences"][experience]["description"]}', border=False, ln=True)
        
    

    pdf.cell(0,10, 'EDUCATION', border=False, ln=True, align='C')
    pdf.cell(0,0, '', border=True, ln=True, align='C')


    # Education
    for education in input_data['education']:

        pdf.cell(0,5, '', border=False, ln=True, align='C')
        pdf.set_font('helvetica', 'B', 14)
        pdf.cell(0,8, f'{input_data["education"][education]["startdate"]} - {input_data["education"][education]["enddate"]}', border=False, ln=True)
        pdf.set_font('helvetica', '', 16)
        pdf.cell(0,8, f'{input_data["education"][education]["name"]} | {input_data["education"][education]["subject"]}', border=False, ln=True)
        pdf.set_font('helvetica', 'B', 14)
        pdf.cell(0,10, 'Description:', border=False, ln=True)
        pdf.set_font('helvetica', '', 16)
        pdf.cell(0,8, f'{input_data["education"][education]["description"]}', border=False, ln=True)
        

    try: 
        random_number = str(random.randint(0, 99999))
        while (len(random_number) < 5):
            random_number = '0' + random_number
        file_name = 'cv-' + random_number
        pdf.output(f'cv/{file_name}.pdf')
        return file_name
    except:
        print('Błąd: otwaty pdf')


