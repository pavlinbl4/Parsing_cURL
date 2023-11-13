import unittest
import check_downloaded_files


class TestGetKommersantDate(unittest.TestCase):

    def test_page_count(self):
        self.assertEqual(check_downloaded_files.get_kommersant_data('files for test/rezult_1.html',0),3)
        self.assertIsInstance(check_downloaded_files.get_kommersant_data('files for test/rezult_1.html',0),int)