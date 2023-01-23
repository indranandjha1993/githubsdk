import requests


class Client:
    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {'Authorization': 'Token ' + access_token}
        self.base_url = 'https://api.github.com'

    def get_user_repositories(self, username):
        """
        Get the repositories of a user
        """
        url = self.base_url + '/users/' + username + '/repos'
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise ValueError(f'Failed to fetch repositories: {response.json()["message"]}')
        return response.json()

    def create_repository(self, name, description=None, private=False):
        """
        Create a new repository
        """
        data = {
            'name': name,
            'description': description,
            'private': private
        }
        url = self.base_url + '/user/repos'
        response = requests.post(url, json=data, headers=self.headers)
        if response.status_code != 201:
            raise ValueError(f'Failed to create repository: {response.json()["message"]}')
        return response.json()

    def get_repository(self, owner, repo):
        """
        Get the details of a repository
        """
        url = self.base_url + f'/repos/{owner}/{repo}'
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise ValueError(f'Failed to fetch repository: {response.json()["message"]}')
        return response.json()

    def edit_repository(self, owner, repo, name=None, description=None, private=None):
        """
        Edit a repository
        """
        data = {}
        if name:
            data['name'] = name
        if description:
            data['description'] = description
        if private:
            data['private'] = private

        url = self.base_url + f'/repos/{owner}/{repo}'
        response = requests.patch(url, json=data, headers=self.headers)

        if response.status_code != 200:
            raise ValueError(f'Failed to edit repository: {response.json()["message"]}')
        return response.json()

    def delete_repository(self, owner, repo):
        """
        Delete a repository
        """
        url = self.base_url + f'/repos/{owner}/{repo}'
        response = requests.delete(url, headers=self.headers)
        if response.status_code != 204:
            raise ValueError(f'Failed to delete repository: {response.json()["message"]}')
        return response.json()

    def get_commits(self, owner, repo):
        """
        Get the commits of a repository
        """
        url = self.base_url + f'/repos/{owner}/{repo}/commits'
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise ValueError(f'Failed to fetch commits: {response.json()["message"]}')
        return response.json()

    def create_commit(self, owner, repo, message, content, sha):
        """
        Create a new commit
        """
        data = {
            'message': message,
            'content': content,
            'sha': sha
        }
        url = self.base_url + f'/repos/{owner}/{repo}/commits'
        response = requests.post(url, json=data, headers=self.headers)
        if response.status_code != 201:
            raise ValueError(f'Failed to create commit: {response.json()["message"]}')

    def get_commit(self, owner, repo, sha):
        """
        Get the details of a specific commit
        """
        url = self.base_url + f'/repos/{owner}/{repo}/commits/{sha}'
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise ValueError(f'Failed to fetch commit: {response.json()["message"]}')
        return response.json()

    def get_branches(self, owner, repo):
        """
        Get the branches of a repository
        """
        url = self.base_url + f'/repos/{owner}/{repo}/branches'
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise ValueError(f'Failed to fetch branches: {response.json()["message"]}')
        return response.json()

    def get_branch(self, owner, repo, branch):
        """
        Get the details of a specific branch
        """
        url = self.base_url + f'/repos/{owner}/{repo}/branches/{branch}'
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise ValueError(f'Failed to fetch branch: {response.json()["message"]}')
        return response.json()

    def create_issue(self, owner,repo, title, body, assignees=None, labels=None, milestone=None):
        """
        Create a new issue
        """
        data = {
            'title': title,
            'body': body
        }
        if assignees:
            data['assignees'] = assignees
        if labels:
            data['labels'] = labels
        if milestone:
            data['milestone'] = milestone

        url = self.base_url + f'/repos/{owner}/{repo}/issues'
        response = requests.post(url, json=data, headers=self.headers)
        if response.status_code != 201:
            raise ValueError(f'Failed to create issue: {response.json()["message"]}')
        return response.json()

    def get_issues(self, owner, repo):
        """
        Get the issues of a repository
        """
        url = self.base_url + f'/repos/{owner}/{repo}/issues'
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise ValueError(f'Failed to fetch issues: {response.json()["message"]}')
        return response.json()

    def get_issue(self, owner, repo, issue_number):
        """
        Get the details of a specific issue
        """
        url = self.base_url + f'/repos/{owner}/{repo}/issues/{issue_number}'
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise ValueError(f'Failed to fetch issue: {response.json()["message"]}')
        return response.json()

    def edit_issue(self, owner, repo, issue_number, title=None, body=None, state=None, assignees=None, labels=None,
                   milestone=None):
        """
        Edit an issues of a repository
        """
        data = {}
        if title:
            data['title'] = title
        if body:
            data['body'] = body
        if state:
            data['state'] = state
        if assignees:
            data['assignees'] = assignees
        if labels:
            data['labels'] = labels
        if milestone:
            data['milestone'] = milestone

        url = self.base_url + f'/repos/{owner}/{repo}/issues/{issue_number}'
        response = requests.patch(url, json=data, headers=self.headers)
        if response.status_code != 200:
            raise ValueError(f'Failed to edit issue: {response.json()["message"]}')
        return response.json()

    def add_collaborator(self, owner, repo, username):
        """
        Add a collaborator to a repository
        """
        data = {'username': username}
        url = self.base_url + f'/repos/{owner}/{repo}/collaborators/{username}'
        response = requests.put(url, json=data, headers=self.headers)
        if response.status_code != 204:
            raise ValueError(f'Failed to add collaborator: {response.json()["message"]}')
        return response.json()

    def remove_collaborator(self, owner, repo, username):
        """
        Remove a collaborator from a repository
        """
        url = self.base_url + f'/repos/{owner}/{repo}/collaborators/{username}'
        response = requests.delete(url, headers=self.headers)
        if response.status_code != 204:
            raise ValueError(f'Failed to remove collaborator: {response.json()["message"]}')
        return response.json()



