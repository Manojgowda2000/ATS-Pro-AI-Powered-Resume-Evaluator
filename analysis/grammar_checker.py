import language_tool_python

def check_grammar(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    issues = [{"message": match.message, "offset": match.offset, "error": match.context} for match in matches]
    return issues