import json


def read_json_file(file_path):
    """
    Read a json file and return the json data
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def write_json_file(file_path, data):
    """
    Write json data to a file
    """
    with open(file_path, 'w') as file:
        json.dump(data, file)


def validate_json(json_data, json_schema):
    """
    Validate json data against a json schema
    """
    import jsonschema
    try:
        jsonschema.validate(json_data, json_schema)
    except jsonschema.exceptions.ValidationError as e:
        raise ValueError(f'Failed to validate json: {e}')


def generate_access_token(client_id, client_secret):
    """
    Generate an access token using client_id and client_secret
    """
    import requests
    data = {
        'client_id': client_id,
        'client_secret': client_secret
    }
    response = requests.post('https://github.com/login/oauth/access_token', json=data)

    if response.status_code != 200:
        raise ValueError(f'Failed to generate access token: {response.json()["message"]}')
    return response.json()['access_token']


def paginate(endpoint, headers, params=None):
    """
    Paginate through API results
    """
    import requests
    while endpoint:
        response = requests.get(endpoint, headers=headers, params=params)
        yield response.json()
        if "link" in response.headers:
            links = parse_link_header(response.headers["link"])
            if 'next' in links:
                endpoint = links['next']['url']
            else:
                endpoint = None
        else:
            endpoint = None


def parse_link_header(header):
    """
    Parse the Link header from the API
    """
    links = {}
    for link in header.split(","):
        (url, rel) = link.split(";")[:2]
        links[rel[5:-1]] = {'url': url[1:-1]}
    return links
