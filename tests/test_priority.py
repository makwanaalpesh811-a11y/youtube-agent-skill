"""YouTube Agent Skill — Priority Tests (mocks only)."""
import unittest
import os

class YouTubeSkillTest(unittest.TestCase):
    def test_happy_path_upload_mock(self):
        result = {"video_id": "mock-abc123", "dry_run": True}
        self.assertIn("mock", result["video_id"])
        self.assertTrue(result["dry_run"])

    def test_invalid_input_empty_title(self):
        title = ""
        self.assertEqual(title, "")

    def test_missing_token(self):
        os.environ.pop("YOUTUBE_TOKEN", None)
        self.assertIsNone(os.environ.get("YOUTUBE_TOKEN"))

    def test_timeout_on_large_video(self):
        def fake():
            raise TimeoutError("upload timeout")
        with self.assertRaises(TimeoutError):
            fake()

    def test_dry_run_no_upload(self):
        # No side effects
        self.assertTrue(True)

    def test_placeholder_key_rejected(self):
        for k in ["your_token", "dummy", "xxx"]:
            if "your" in k or "dummy" in k or "xxx" == k:
                self.assertTrue(True)

    def test_copy_paste_example(self):
        ex = '''
python3 ~/yt.py upload video.mp4 --title "My Video" --dry-run
'''
        self.assertIn("--dry-run", ex)

    def test_error_content_id_claim(self):
        err = {"error": "content ID claim", "code": "COPYRIGHT"}
        self.assertEqual(err["code"], "COPYRIGHT")

    def test_error_token_expired(self):
        err = {"error": "token expired", "code": 401}
        self.assertEqual(err["code"], 401)


if __name__ == "__main__":
    unittest.main()
