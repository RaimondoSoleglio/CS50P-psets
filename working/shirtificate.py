from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style="B", size=30)
        # Printing title:
        self.cell(120, 30, "CS50 Shirtificate", border=1, align="C", center=True)
        # Performing a line break:
        self.ln(50)


def main():
    name = input("What's your name? ")
    text = f"{name} took CS50"

    pdf = PDF()
    pdf.add_page()
    pdf.image("shirtificate.png", w=pdf.epw)
    pdf.set_font("helvetica", style="B", size=23)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.cell(h=-250, text=text, center=True)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
