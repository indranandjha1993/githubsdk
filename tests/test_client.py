import unittest
from github_sdk.client import Client


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client(
            access_token='')

    def test_get_user(self):
        user = self.client.get_user_repositories('indranandjha1993')
        self.assertEqual(user['login'], 'indranandjha1993')

    def test_get_repo(self):
        repo = self.client.get_repository('indranandjha1993', 'githubsdk')
        self.assertEqual(repo['name'], 'githubsdk')

    def test_create_repo(self):
        repo = self.client.create_repository('test-repo-2', 'This is a test repository', 'indranandjha1993')
        self.assertEqual(repo['name'], 'test-repo-2')
        self.assertEqual(repo['owner']['login'], 'indranandjha1993')

    def test_get_commits(self):
        commits = self.client.get_commits('indranandjha1993', 'test-repo')
        self.assertGreaterEqual(len(commits), 0)

    def test_get_branches(self):
        branches = self.client.get_branches('indranandjha1993', 'test-repo')
        self.assertGreaterEqual(len(branches), 0)

    def test_create_issue(self):
        issue = self.client.create_issue('indranandjha1993', 'test-repo', 'test issue', 'This is a test issue')
        self.assertEqual(issue['title'], 'test issue')
        self.assertEqual(issue['body'], 'This is a test issue')

    def test_get_issues(self):
        issues = self.client.get_issues('indranandjha1993', 'test-repo')
        self.assertGreaterEqual(len(issues), 0)


if __name__ == 'main':
    unittest.main()
