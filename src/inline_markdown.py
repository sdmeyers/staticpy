import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        node_text_list = old_node.text.split(delimiter)
        if len(node_text_list) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(node_text_list)):
            if node_text_list[i] == "":
                continue
            if i % 2 == 0: # Even items should be TEXT
                split_nodes.append(TextNode(node_text_list[i], TextType.TEXT))
            else: # Odd items should be text_type
                split_nodes.append(TextNode(node_text_list[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
