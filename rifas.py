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

                # If booked -> write "vendido"
                if current in booked_numbers:
                    c.setFont("Helvetica-Bold", 10)
                    c.setFillColor(colors.red)

                    c.drawCentredString(
                        x + rect_width / 2,
                        y + rect_height / 2 - 4,
                        "vendido"
                    )

                    # Reset style
                    c.setFillColor(colors.black)

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

booked = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
          38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 57, 58, 63, 67, 68, 69, 73, 77, 78, 84, 88, 89, 90, 91, 95, 97, 98,
          100, 101, 101, 103, 105, 112, 115, 117, 118, 119, 123, 124, 127, 128, 130, 135, 145, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161,
          162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 183, 184, 185, 194, 197, 198, 199, 200]

create_numbered_pdf(
    output_path="rifas.pdf",
    ranges=number_ranges,
    booked_numbers=booked
)


print("PDF generated successfully!")
