# GitHub SDK

This is an SDK for interacting with the GitHub API in Python.
It provides a simple and easy to use interface for making requests to the API and handling responses.

## Installation

You can install the SDK using pip:

```bash
  pip install git+https://github.com/indranandjha1993/githubsdk.git
```

## Usage

Here is an example of how to use the SDK to get the user details of a specific user:
```python
    from githubsdk import Client
    
    client = Client(access_token='your_access_token')
    user = client.get_user('indranandjha1993')
    print(user)
```

You can also use the SDK to interact with other parts of the GitHub API like repository, commits, branches,
issues, collaborators, etc.

## Dependencies
This SDK requires the following dependencies:

    requests
    jsonschema
