from PIL import Image, ImageFont, ImageDraw


def add_text(words, img):
    #set a maximum width, line spacing and font size
    max_width = img.size[0] * 0.95
    space = 2.5
    font_size = 40

    line = ""
    lines = []

    #define font to use
    text_font = ImageFont.truetype("DejaVuSans.ttf", font_size)

    #split text into lines
    for word in words:
        if line: #line not empty
            test_line = line + " " + word
        else: #line empty
            test_line = word

        #get current line width
        width = text_font.getlength(test_line)
        #check current line witdh against maximum width and update 
        if width <= max_width: #not too big
            line = test_line
        else:
            lines.append(line) #too big
            line = word
    if line: lines.append(line) #add last line to lines

    quote = "\n".join(lines) #text string separated by new line

    x_pos = (img.size[0] - max_width) / 2 #x starting coord of text

    y_pos = img.size[1] #y starting coord of text
    for l in lines:
        y_pos -= (space + font_size + (3 * 2))
    y_pos -= x_pos - space
    if y_pos >= img.size[1] * 0.75: y_pos = img.size[1] * 0.75 #adjust if low

    draw = ImageDraw.Draw(img)
    draw.text((x_pos, y_pos), quote, font=text_font, spacing=space, fill="white", stroke_width=3, stroke_fill="black")

    img.save("pictures/test.png")
