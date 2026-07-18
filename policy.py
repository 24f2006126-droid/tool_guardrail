def check_bash(command):
    return {
        "decision": "allow",
        "reason": "Command allowed."
    }


def check_write(path):
    return {
        "decision": "allow",
        "reason": "Write allowed."
    }


def check_http(url):
    return {
        "decision": "allow",
        "reason": "Host allowed."
    }


def evaluate(request):

    tool = request["tool"]

    if tool == "bash":
        return check_bash(request["command"])

    if tool == "write_file":
        return check_write(request["path"])

    if tool == "http_request":
        return check_http(request["url"])

    return {
        "decision": "block",
        "reason": "Unknown tool."
    }