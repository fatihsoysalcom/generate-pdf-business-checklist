from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

def generate_checklist_pdf(filename="business_checklist.pdf"):
    """Generates a PDF business checklist from a predefined data structure."""

    # 1. Document setup: Create a new PDF document with A4 page size
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    story = [] # This list will hold all the elements (flowables) for the PDF

    # Define custom paragraph styles for sections and checklist items
    styles.add(ParagraphStyle(name='ChecklistItem',
                              parent=styles['Normal'],
                              fontSize=10,
                              leading=14,
                              leftIndent=20))
    styles.add(ParagraphStyle(name='ChecklistSection',
                              parent=styles['h2'],
                              fontSize=14,
                              leading=18,
                              spaceAfter=6,
                              spaceBefore=12))

    # 2. Data structure: A list of dictionaries representing checklist sections and items
    # The article emphasizes using a single data structure for hundreds of items.
    checklist_data = [
        {"type": "section", "title": "Proje Başlangıcı (Project Start)"},
        {"type": "item", "text": "Gereksinimler toplandı ve onaylandı (Requirements gathered and approved)"},
        {"type": "item", "text": "Proje planı oluşturuldu (Project plan created)"},
        {"type": "item", "text": "Ekip üyeleri belirlendi (Team members identified)"},
        {"type": "item", "text": "Kaynaklar tahsis edildi (Resources allocated)"},
        {"type": "item", "text": "Paydaşlar bilgilendirildi (Stakeholders informed)"},

        {"type": "section", "title": "Geliştirme Süreci (Development Process)"},
        {"type": "item", "text": "Kodlama standartlarına uyuldu (Coding standards followed)"},
        {"type": "item", "text": "Birim testleri yazıldı (Unit tests written)"},
        {"type": "item", "text": "Entegrasyon testleri yapıldı (Integration tests performed)"},
        {"type": "item", "text": "Kod incelemesi yapıldı (Code review conducted)"},
        {"type": "item", "text": "Sürüm kontrol sistemi kullanıldı (Version control system used)"},
        {"type": "item", "text": "Dokümantasyon güncellendi (Documentation updated)"},

        {"type": "section", "title": "Test ve Kalite Kontrol (Testing & Quality Control)"},
        {"type": "item", "text": "Fonksiyonel testler tamamlandı (Functional tests completed)"},
        {"type": "item", "text": "Performans testleri yapıldı (Performance tests conducted)"},
        {"type": "item", "text": "Güvenlik açıkları kontrol edildi (Security vulnerabilities checked)"},
        {"type": "item", "text": "Hata takibi ve düzeltme yapıldı (Bug tracking and fixing performed)"},
        {"type": "item", "text": "Kullanıcı kabul testleri (UAT) tamamlandı (User Acceptance Tests completed)"},

        {"type": "section", "title": "Dağıtım ve Bakım (Deployment & Maintenance)"},
        {"type": "item", "text": "Test ortamında dağıtım yapıldı (Deployed to test environment)"},
        {"type": "item", "text": "Üretim ortamına dağıtım planı hazırlandı (Production deployment plan prepared)"},
        {"type": "item", "text": "Yedekleme prosedürleri kontrol edildi (Backup procedures checked)"},
        {"type": "item", "text": "İzleme ve günlük kaydı ayarları yapıldı (Monitoring and logging configured)"},
        {"type": "item", "text": "Destek ekibi bilgilendirildi (Support team informed)"},
        {"type": "item", "text": "Periyodik bakım planı oluşturuldu (Periodic maintenance plan created)"}
    ]

    # Add a main title to the PDF
    story.append(Paragraph("İş Kontrol Listesi (Business Checklist)", styles['h1']))
    story.append(Spacer(1, 0.2 * inch))

    # 3. Iterate through the data structure and add elements to the PDF story
    for item in checklist_data:
        if item["type"] == "section":
            # Add a section title using the custom style
            story.append(Paragraph(item["title"], styles['ChecklistSection']))
            story.append(Spacer(1, 0.1 * inch))
        elif item["type"] == "item":
            # Add a checklist item with a checkbox placeholder and item text
            story.append(Paragraph(f"[ ] {item['text']}", styles['ChecklistItem']))
            story.append(Spacer(1, 0.05 * inch)) # Smaller space between items

    # 4. Build the PDF document from the story
    doc.build(story)
    print(f"Checklist PDF '{filename}' generated successfully.")

if __name__ == "__main__":
    generate_checklist_pdf()
