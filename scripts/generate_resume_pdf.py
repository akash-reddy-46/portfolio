#!/usr/bin/env python3
"""Build assets/Vanga-Akash-Reddy-Resume.pdf from portfolio-aligned copy."""

from pathlib import Path

from fpdf import FPDF

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "Vanga-Akash-Reddy-Resume.pdf"


class ResumePDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_margins(18, 18, 18)
        self.set_auto_page_break(auto=True, margin=14)

    def heading_block(self, title: str, subtitle: str | None = None) -> None:
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(25, 35, 55)
        self.cell(0, 5.5, title, ln=1)
        if subtitle:
            self.set_font("Helvetica", "I", 9)
            self.set_text_color(70, 80, 100)
            self.cell(0, 4.5, subtitle, ln=1)
        self.set_text_color(0, 0, 0)
        self.set_font("Helvetica", "", 9)
        self.ln(1)

    def bullets(self, lines: list[str]) -> None:
        self.set_font("Helvetica", "", 9)
        left = self.l_margin + 3
        usable = self.w - self.r_margin - left
        for line in lines:
            self.set_x(left)
            self.multi_cell(usable, 4.3, "- " + line)
        self.ln(1)


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)

    pdf = ResumePDF()
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 17)
    pdf.cell(0, 8, "VANGA AKASH REDDY", ln=1)
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 5, "Backend / Software Engineer", ln=1)
    pdf.set_font("Helvetica", "", 9)
    for line in (
        "Hyderabad, Telangana, India",
        "vangaakashreddy@gmail.com | +91-77992-18720",
        "linkedin.com/in/akash-reddy-vanga-49377b358 | github.com/akash-reddy-46",
        "Portfolio: akash-reddy-46.github.io/portfolio/",
    ):
        pdf.cell(0, 4.3, line, ln=1)

    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "SUMMARY", ln=1)
    pdf.set_font("Helvetica", "", 9)
    pdf.multi_cell(
        0,
        4.5,
        "3+ years shipping production backend systems at JaaGa.AI using Node.js, AWS, and MongoDB. "
        "Owns payments (Cashfree webhooks, retries, reconciliation), automation, OCR/Lambda document pipelines, "
        "WhatsApp notifications, and backend/AWS behind www.jaaga.ai. Strong focus on idempotency, observability, "
        "and on-call reliability. Open to Backend, Platform, or DevOps roles.",
    )

    pdf.ln(1)
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "EXPERIENCE", ln=1)

    pdf.heading_block(
        "Software Engineer",
        "JaaGa.AI | Hyderabad, India | Apr 2026 - Present (promoted)",
    )
    pdf.bullets(
        [
            "Own backend services for payments, automation, and notifications: API design, data modeling, deployment, monitoring, on-call.",
            "Built and operate backend and AWS for www.jaaga.ai (e.g. Lambda, S3, integrations, deployment/ops) alongside core products.",
            "Architected payment retry + reconciliation; reduced failure rate from 2.8% to 0.3% across 10K+ monthly transactions.",
            "Write and maintain runbooks; first-line on-call; blameless post-mortems with clear follow-ups.",
            "Partner with finance, ops, product, and legal to turn business asks into shippable specs.",
        ]
    )

    pdf.heading_block(
        "Backend Developer",
        "JaaGa.AI | Hyderabad, India | Apr 2024 - Apr 2026",
    )
    pdf.bullets(
        [
            "Shipped production services on AWS, MongoDB, and Node.js handling INR 50L+ monthly payment volume.",
            "Integrated Cashfree end-to-end: checkout, webhook verification, idempotent retries with backoff, reconciliation.",
            "Built WhatsApp notification service with template fallbacks and queue-backed retries (~98.5% delivery at peak).",
            "Tuned MongoDB indexes/aggregations and Node.js hot paths to reduce latency under load.",
        ]
    )

    pdf.heading_block(
        "Backend Developer Intern",
        "JaaGa.AI | Hyderabad, India | Oct 2023 - Mar 2024",
    )
    pdf.bullets(
        [
            "Delivered REST APIs with Node.js, Express, and MongoDB; production-facing features within the first 3 months.",
            "Schemas, validation, and queries for new modules; deployment discipline and real incident debugging.",
            "Converted to full-time based on ownership on lawyer-document and billing modules.",
        ]
    )

    pdf.add_page()
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "SELECTED PROJECT IMPACT (PRODUCTION)", ln=1)
    pdf.set_font("Helvetica", "", 9)
    pdf.bullets(
        [
            "Payments platform: ~99.7% success rate; robust webhook handling and reconciliation.",
            "Lawyer document pipeline: S3 -> Lambda OCR -> MongoDB with PM2 workers and retries; strong OCR accuracy, reduced manual work.",
            "Property document automation: templating, Google Sheets integration, PDF generation to S3.",
            "Internal notification/webhook platforms with reliable delivery at scale.",
        ]
    )

    pdf.ln(1)
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "TECHNICAL SKILLS", ln=1)
    pdf.set_font("Helvetica", "", 9)
    pdf.multi_cell(
        0,
        4.5,
        "Languages & runtime: JavaScript, Node.js | Frameworks: Express.js | Data: MongoDB (modeling, indexing, aggregations) "
        "| Cloud & ops: AWS (Lambda, S3, EC2), Docker, CI/CD, PM2 | Integrations: Cashfree, REST APIs, webhooks "
        "| Practices: idempotency, retries, observability, incident response | Tools: Git, Bash/Linux.",
    )

    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "EDUCATION", ln=1)
    pdf.set_font("Helvetica", "", 9)
    pdf.cell(0, 4.5, "Master of Computer Applications (MCA) | Osmania University, Hyderabad | 2025 - 2027", ln=1)

    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "CERTIFICATIONS & LEARNING", ln=1)
    pdf.set_font("Helvetica", "", 9)
    pdf.multi_cell(
        0,
        4.5,
        "Introduction to Databases | AI Fundamentals | Build Your Own Responsive Website | "
        "Build Your Own Static Website | AI for Brainstorming and Planning",
    )

    pdf.ln(3)
    pdf.set_font("Helvetica", "I", 8)
    pdf.multi_cell(
        0,
        4,
        "Declaration: The information above is accurate to the best of my knowledge.",
    )
    pdf.set_font("Helvetica", "", 9)
    pdf.cell(0, 5, "Place: Hyderabad", ln=1)
    pdf.cell(0, 5, "(Vanga Akash Reddy)", ln=1)

    pdf.output(str(OUT))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
