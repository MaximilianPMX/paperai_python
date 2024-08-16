import unittest
from paperai.src.paperai.report_generator import ReportGenerator

class TestReportGenerator(unittest.TestCase):

    def test_generate_report_with_empty_data(self):
        generator = ReportGenerator()
        data = {}
        report = generator.generate_report(data)
        self.assertEqual(report, "No data to report.")

    def test_generate_report_with_basic_data(self):
        generator = ReportGenerator()
        data = {
            "title": "Sample Paper",
            "abstract": "This is a sample abstract.",
            "sections": [
                {"heading": "Introduction", "content": "This is the introduction."},
                {"heading": "Conclusion", "content": "This is the conclusion."}
            ]
        }
        report = generator.generate_report(data)
        self.assertIn("Sample Paper", report)
        self.assertIn("This is a sample abstract.", report)
        self.assertIn("Introduction", report)
        self.assertIn("This is the introduction.", report)
        self.assertIn("Conclusion", report)
        self.assertIn("This is the conclusion.", report)

    def test_generate_report_with_no_sections(self):
        generator = ReportGenerator()
        data = {
            "title": "Sample Paper",
            "abstract": "This is a sample abstract."
        }
        report = generator.generate_report(data)
        self.assertIn("Sample Paper", report)
        self.assertIn("This is a sample abstract.", report)
        self.assertNotIn("Introduction", report) # Ensure no section related text accidentally slips in.

    def test_generate_report_with_empty_sections(self):
        generator = ReportGenerator()
        data = {
            "title": "Sample Paper",
            "abstract": "This is a sample abstract.",
            "sections": []
        }
        report = generator.generate_report(data)
        self.assertIn("Sample Paper", report)
        self.assertIn("This is a sample abstract.", report)
        self.assertNotIn("Introduction", report) # Ensure no section related text accidentally slips in.

    def test_generate_report_with_missing_data(self):
        generator = ReportGenerator()
        data = {
            "title": "Sample Paper",
        }
        report = generator.generate_report(data)
        self.assertIn("Sample Paper", report)
        self.assertNotIn("This is a sample abstract.", report)
        self.assertNotIn("Introduction", report)

if __name__ == '__main__':
    unittest.main()
