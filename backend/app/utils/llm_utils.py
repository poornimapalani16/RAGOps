def get_response_text(response) -> str:
    content = response.content

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        texts = []

        for item in content:
            if isinstance(item, dict) and "text" in item:
                texts.append(item["text"])

        return "\n".join(texts)

    return str(content)