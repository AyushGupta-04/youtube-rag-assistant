from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet , ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether 

def generate_mcq_pdf(mcqs,difficulty,video_url=None):
    """
    Generate a PDF containing MCQ questions, options, answers, and explanations.
    Returns:
        bytes
    """
    buffer = BytesIO()
    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title="YouTube AI MCQ Quiz",
        author="YouTube AI"
    )

    styles = getSampleStyleSheet()
    # STYLES
    title_style = ParagraphStyle(
        "QuizTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=27,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#222222"),
        spaceAfter=8
    )

    subtitle_style = ParagraphStyle(
        "QuizSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#666666"),
        spaceAfter=18
    )

    question_style = ParagraphStyle(
        "Question",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=16,
        textColor=colors.HexColor("#222222"),
        spaceAfter=8
    )

    option_style = ParagraphStyle(
        "Option",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=15,
        leftIndent=8,
        textColor=colors.HexColor("#333333"),
        spaceAfter=4
    )

    answer_style = ParagraphStyle(
        "Answer",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=15,
        textColor=colors.HexColor("#198754"),
        spaceAfter=4
    )

    explanation_style = ParagraphStyle(
        "Explanation",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=15,
        textColor=colors.HexColor("#444444"),
        spaceAfter=12
    )

    section_style = ParagraphStyle(
        "Section",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=20,
        textColor=colors.HexColor("#222222"),
        spaceAfter=15
    )
    # CONTENT
    story = []

    # HEADER
    story.append(Paragraph("MCQ", title_style))
    story.append(Paragraph("Multiple Choice Quiz",subtitle_style))
    story.append(Paragraph(f"<b>Difficulty:</b> {difficulty}",styles["Normal"]))
    story.append(Paragraph(f"<b>Total Questions:</b> {len(mcqs)}", styles["Normal"] ))

    story.append(Spacer(1, 10))
    story.append(Paragraph("Quiz Questions",section_style ))

    # QUESTIONS
    for index, mcq in enumerate(mcqs):
        question_number = index + 1
        question_block = [ 
            Paragraph(f"<b>{question_number}." f"{mcq.question} </b>", question_style,),
            Paragraph(f"A. {mcq.option_a}",option_style),
            Paragraph(f"B. {mcq.option_b}",option_style),
            Paragraph(f"C. {mcq.option_c}",option_style),
            Paragraph(f"D. {mcq.option_d}",option_style),
            Spacer(1, 10)
        ]

        story.append(KeepTogether(question_block))

    # ANSWER KEY
    story.append(PageBreak())
    story.append(Paragraph("Answer Key & Explanations",section_style))

    for index, mcq in enumerate(mcqs):
        question_number = index + 1

        story.append(Paragraph(f"{question_number}. "
                               f"Correct Answer: "
                               f"{mcq.correct_answer}",
                               answer_style)
                               )

        story.append( 
            Paragraph(f"<b>Explanation:</b> " f"{mcq.explanation}", explanation_style 
                      ))

    # BUILD
    document.build(story)
    buffer.seek(0)
    return buffer.getvalue()