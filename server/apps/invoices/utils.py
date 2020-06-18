from fpdf import FPDF


def get_invoice_pdf_str(invoice) -> str:
    """Return string representation of generated PDF file for Invoice"""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'I', size=40)
    pdf.cell(w=0, txt=f'Invoice #{invoice.id}', align='C', ln=1)
    pdf.dashed_line(5, 20, pdf.w - 5, 20)
    pdf.set_font('Arial', size=20)
    pdf.ln(20)
    sum_ = 0
    for position in invoice.positions.all():
        pdf.cell(w=0, txt=position.product.title, align='L')
        pdf.cell(
            w=0,
            txt=f'{position.price}$ * {position.quantity} = '
                f'{position.quantity * position.price}$',
            align='R'
        )
        pdf.ln(10)
        sum_ += position.quantity * position.price
    pdf.dashed_line(5, pdf.get_y(), pdf.w - 5, pdf.get_y())
    pdf.ln(10)
    pdf.cell(w=0, txt='Summary:', align='L')
    pdf.cell(w=0, txt=f'{sum_}$', align='R')

    return pdf.output(dest='S').encode('latin-1')
