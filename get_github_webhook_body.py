def get_github_body_str(payload):
    result = ""
    if payload.get('action'):
        result += 'Action: ' + str(payload['action']) + "\n"
    if payload.get('comment'):
        result += 'Comment: ' + str(payload['comment']) + "\n"
    if payload.get('issue'):
        issue = payload['issue']
        issue_number = issue.get('number')
        issue_title = issue.get('title')
        issue_sender = issue.get('user', dict()).get('login')
        if issue_number and issue_title:
            result += 'New Issue #' + str(issue_number) + ': ' + str(issue_title) + '\n'
        if issue_sender:
            result += "Issue Submitted By: " + str(issue_sender) + '\n'
    if payload.get('repository'):
        repository = payload['repository']
        if repository.get('name'):
            result += 'Repository: ' + str(repository['name']) + '\n'
    if payload.get('sender'):
        if payload.get('login'):
            result += "By: " + payload['sender']['login']
            result += "\n"

    # Add Commit Message:
    if payload.get('commits'):
        commits = payload['commits']
        if type(commits) == list:
            for commit in commits:
                commit_message = commit.get('message')
                commit_author = commit.get('committer', dict())
                commit_author_name = commit_author.get('name')
                commit_author_username = commit_author.get('username')
                commit_url = commit.get('url')
                if commit_message and commit_author_name and commit_author_username and commit_url:
                    result += "New Commit: " + commit_message + "\n\tBy: " + commit_author_name \
                              + ", " + commit_author_username + "\n\tAt: " + commit_url
                elif commit_url:
                    result += "New Commit: " + commit_url
                else:
                    result += "New Commit"
                result += "\n"

    return result
