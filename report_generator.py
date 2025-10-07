from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import pandas as pd
from io import BytesIO
from datetime import datetime

def generate_pdf_report(data: pd.DataFrame, title: str) -> BytesIO:
    """
    Genera un informe en PDF a partir de un DataFrame de Pandas.

    Args:
        data (pd.DataFrame): Los datos para el informe.
        title (str): El título del informe.

    Returns:
        BytesIO: El buffer de bytes que contiene el PDF.
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    # Título del reporte
    elements.append(Paragraph(title, styles['h1']))
    elements.append(Spacer(1, 12))

    # Fecha de generación
    generation_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    elements.append(Paragraph(f"Generado el: {generation_date}", styles['Normal']))
    elements.append(Spacer(1, 24))

    # Convertir DataFrame a una lista de listas para la tabla
    if not data.empty:
        table_data = [data.columns.to_list()] + data.values.tolist()
        
        # Estilo de la tabla
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])
        
        # Crear y añadir la tabla
        table = Table(table_data)
        table.setStyle(style)
        elements.append(table)
    else:
        elements.append(Paragraph("No se encontraron datos para este informe.", styles['Normal']))

    doc.build(elements)
    buffer.seek(0)
    return buffer
