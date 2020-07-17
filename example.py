from get_github_webhook_body import get_github_body_str
import json


if __name__ == "__main__":
    with open('examples/payload_issue_example.json', 'r') as json_file:
        payload = json.load(json_file)
        print(get_github_body_str(payload))
