from textnode import TextNode, TextType

def main():
    dumb_text1 = TextNode("This is anchor text", TextType.LINK, "http://mydogateit.com")
    print(dumb_text1)

main()
