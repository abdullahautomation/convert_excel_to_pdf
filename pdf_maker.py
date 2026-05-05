from fpdf import FPDF
import pandas as pd
def excel_to_pdf(input_file, output_file):
    df = pd.read_excel(input_file)
    # for col in df.columns:
    #     print(col, df[col].astype(str).str.len().max())
    # print(df["Product"].astype(str).str.len())
    df_widths = []
    class MyPDF(FPDF):
        def header(self):
            if self.page_no() == 1:
                self.set_font("Helvetica", style="B", size=18)
                self.cell(277,7, text="Automation Lab",align="CENTER", new_x="LMARGIN", new_y="NEXT")
                self.set_font("Helvetica", style="B", size=12)
                self.cell(277,10, text="Converting manual complex tasks in Automations", align="CENTER", new_x="LMARGIN", new_y="NEXT")
            self.set_fill_color(255, 255, 0)
            self.set_font("Helvetica", size=12)
            for col, width in zip(df.columns, df_widths):
                self.cell(width, 10, text=col, border=1, fill=True, new_x="RIGHT", new_y="TOP")
            self.ln()
    page_width = 277
    for col in df.columns:
        max_length = max(df[col].astype(str).str.len().max(), len(col))
        width = max_length * 5 + 10
        df_widths.append(width)
    total_width = sum(df_widths)
    df_widths = [w * page_width/ total_width for w in df_widths]
    # print(df_widths)
    pdf = MyPDF(orientation="L")
    pdf.add_page()

    for _,row in df.iterrows():
        for value, width in zip(row, df_widths):
            pdf.cell(width, 10, text=str(value), border=1, new_x="RIGHT", new_y="TOP")
        pdf.ln()
    pdf.output(output_file)
    print("PDF DONE!")
if __name__ == "__main__":
    # a = str(input("Enter Input file name(with.xlsx): "))
    # b = str(input("Enter Output file name(with.pdf): "))
    # excel_to_pdf(a,b)
    excel_to_pdf("output.xlsx", "pdf_maker.pdf")