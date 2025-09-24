# runner.py
import unittest
import HtmlTestRunner

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover("tests")  # carpeta con tus .py
    runner = HtmlTestRunner.HTMLTestRunner(
        output="reports",
        report_name="reporte_unittest",
        report_title="SauceDemo - Resultados",
        combine_reports=True,
        add_timestamp=True
    )
    runner.run(suite)
