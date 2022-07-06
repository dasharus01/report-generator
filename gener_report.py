from docxtpl import DocxTemplate
doc = DocxTemplate("template.docx")
context = { 'name' : "И.И.Иванов"}
doc.render(context)
doc.save("report.docx")


