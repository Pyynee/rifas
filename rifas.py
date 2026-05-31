from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib import colors


def create_numbered_pdf(output_path, ranges, booked_numbers=None):
    """
    Create a PDF with numbered rectangles.

    Parameters:
    - output_path: path of the PDF file
    - ranges: list of tuples with start/end numbers
    Example: [(1, 50), (51, 100)]
    - booked_numbers: list or set of numbers to mark with a cross
    """

    if booked_numbers is None:
        booked_numbers = []

    booked_numbers = set(booked_numbers)

    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    margin_x = 15 * mm
    margin_y = 15 * mm

    for page_index, (start_num, end_num) in enumerate(ranges):

        cols = 5
        rows = 10

        usable_width = width - 2 * margin_x
        usable_height = height - 2 * margin_y

        rect_width = usable_width / cols
        rect_height = usable_height / rows

        current = start_num

        for r in range(rows):
            for col in range(cols):

                if current > end_num:
                    break

                x = margin_x + col * rect_width
                y = height - margin_y - (r + 1) * rect_height

                # Draw rectangle
                c.rect(x, y, rect_width, rect_height)

                # Draw number in top-right corner
                c.setFont("Helvetica-Bold", 9)
                c.drawRightString(
                    x + rect_width - 5,
                    y + rect_height - 11,
                    str(current)
                )

                # If booked -> draw X cross
                if current in booked_numbers:
                    c.setStrokeColor(colors.red)
                    c.setLineWidth(2)

                    c.line(x + 5, y + 5,
                           x + rect_width - 5, y + rect_height - 5)

                    c.line(x + 5, y + rect_height - 5,
                           x + rect_width - 5, y + 5)

                    # Reset style
                    c.setStrokeColor(colors.black)
                    c.setLineWidth(1)

                current += 1

        if page_index < len(ranges) - 1:
            c.showPage()

    c.save()


# -----------------------------
# RUN THE SCRIPT
# -----------------------------

number_ranges = [
    (1, 50),
    (51, 100),
    (101, 150),
    (151, 200),
    (201, 250)
]

booked = [1, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 21, 23, 24, 25, 26, 27, 29, 31, 32, 36, 40,
          43, 46, 49, 50, 51, 54, 57, 63, 69, 73, 77, 84, 88, 100, 103, 101, 103, 105, 112, 115, 117, 127, 
          135, 148, 151, 152, 153, 154, 155, 172, 184, 197,200]

create_numbered_pdf(
    output_path="rifas.pdf",
    ranges=number_ranges,
    booked_numbers=booked
)


print("PDF generated successfully!")
