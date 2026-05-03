from fpdf import FPDF
import pandas as pd
def excel_to_pdf(input_file, output_file):
    df = pd.read_excel(input_file)
    class MyPDF(FPDF):
        def header(self):
            if self.page_no() == 1:
                pdf.set_font("Helvetica", style="B", size=22)
                pdf.cell(200, 5, text="Automation Lab", align="CENTER", new_x="LMARGIN", new_y="NEXT")
                pdf.set_font("Helvetica", style="B", size=12)
                pdf.cell(200, 10, text="We help bussinesses to automate manual time taken tasks.", align="CENTER", new_x="LMARGIN", new_y="NEXT")
            self.set_fill_color(255, 255, 0)
            self.set_font("Helvetica", style="B", size=10)
            # print(df.columns.tolist())
            for col in df.columns:
                self.cell(32, 10, text=col, fill=True, border=1, new_x="RIGHT", new_y="TOP")
            self.ln()

    pdf = MyPDF()
    pdf.add_page()
    


    pdf.set_font("Helvetica", size=10)
    for index, row in df.iterrows():
        for value in row:
            pdf.cell(32, 10, text=str(value), border=1, new_x="RIGHT", new_y="TOP")
        pdf.ln()
    pdf.output(output_file)
    print("PDF Done")
if __name__ == "__main__":
    # a = str(input("Enter Input file name(with.xlsx): "))
    # b = str(input("Enter Output file name(with.pdf): "))
    # excel_to_pdf(a,b)
    excel_to_pdf("output.xlsx", "pdf_maker.pdf")