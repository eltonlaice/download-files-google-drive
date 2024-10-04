import unittest
import os
from main import download_file_from_google_drive

class TestGoogleDriveDownloader(unittest.TestCase):
    def setUp(self):
        self.test_file_id = "1ZdR3L3qP4Bkq8noWLJHSr_iBau0DNT4"
        self.output_directory = "test_downloads"
        os.makedirs(self.output_directory, exist_ok=True)

    def tearDown(self):
        for file in os.listdir(self.output_directory):
            os.remove(os.path.join(self.output_directory, file))
        os.rmdir(self.output_directory)

    def test_download_file(self):
        download_file_from_google_drive(self.test_file_id, self.output_directory)
        downloaded_files = os.listdir(self.output_directory)
        self.assertEqual(len(downloaded_files), 1, "One file should be downloaded")
        self.assertTrue(os.path.getsize(os.path.join(self.output_directory, downloaded_files[0])) > 0, "Downloaded file should not be empty")

    def test_invalid_file_id(self):
        with self.assertRaises(Exception):
            download_file_from_google_drive("invalid_file_id", self.output_directory)

if __name__ == '__main__':
    unittest.main()
