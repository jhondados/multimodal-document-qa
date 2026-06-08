"""Multimodal document Q&A with Gemini Vision."""
from google.genai import Client, types
from pathlib import Path
from typing import List, Dict
import base64, fitz  # PyMuPDF

class MultimodalDocQA:
    def __init__(self):
        self.client = Client()
        self.model = "gemini-2.0-flash-exp"

    def pdf_to_images(self, pdf_path: str, dpi: int = 150) -> List[bytes]:
        """Convert PDF pages to images for visual QA."""
        doc = fitz.open(pdf_path)
        images = []
        for page in doc:
            mat = fitz.Matrix(dpi/72, dpi/72)
            pix = page.get_pixmap(matrix=mat)
            images.append(pix.tobytes("png"))
        return images

    def answer_question(self, question: str, document_path: str, max_pages: int = 20) -> Dict:
        """Answer a question over a multi-modal document."""
        images = self.pdf_to_images(document_path)[:max_pages]
        # Build content with all page images
        content = [f"Document: {Path(document_path).name} ({len(images)} pages)\n\nQuestion: {question}\n\nAnalyze all pages (text, tables, charts, images) to answer comprehensively."]
        for i, img_bytes in enumerate(images):
            content.append(types.Part.from_bytes(data=img_bytes, mime_type="image/png"))
            content.append(f"[Page {i+1}]")
        content.append("\nProvide a detailed answer citing specific page numbers and evidence (text/table/chart).")
        response = self.client.models.generate_content(model=self.model, contents=content)
        return {"answer": response.text, "pages_analyzed": len(images), "document": document_path}

    def extract_table_data(self, image_bytes: bytes) -> str:
        """Extract and structure table data from image."""
        img_part = types.Part.from_bytes(data=image_bytes, mime_type="image/png")
        prompt = "Extract all table data from this image. Return as markdown table with all rows and columns. If multiple tables, extract each separately."
        response = self.client.models.generate_content(model=self.model, contents=[img_part, prompt])
        return response.text
