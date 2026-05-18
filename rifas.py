from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

path = "rectangles_1_to_250.pdf"

c = canvas.Canvas(path, pagesize=A4)
w, h = A4

margin_x = 15 * mm
margin_y = 15 * mm

ranges = [
    (1, 50),
    (51, 100),
    (101, 150),
    (151, 200),
    (201, 250),
]

for idx, (start_num, end_num) in enumerate(ranges):
    cols = 5
    rows = 10

    usable_w = w - 2 * margin_x
    usable_h = h - 2 * margin_y

    rect_w = usable_w / cols
    rect_h = usable_h / rows

    current = start_num

    for r in range(rows):
        for col in range(cols):
            if current > end_num:
                break

            x = margin_x + col * rect_w
            y = h - margin_y - (r + 1) * rect_h

            c.rect(x, y, rect_w, rect_h)

            c.setFont("Helvetica-Bold", 9)
            c.drawRightString(
                x + rect_w - 5,
                y + rect_h - 11,
                str(current)
            )

            current += 1

    if idx < len(ranges) - 1:
        c.showPage()

c.save()

print(f"PDF created: {path}")
