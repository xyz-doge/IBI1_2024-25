#   Import required modules
import xml.sax
import time

#   Define a custom SAX content handler for GO terms
class GOHandler(xml.sax.ContentHandler):
    #   Initialization
    def __init__(self):
        self.current_tag = ""
        self.current_namespace = ""
        self.current_name = ""
        self.current_is_a_count = 0

        #   Store the max <is_a> count and name for each GO category
        self.max_is_a = {
            "molecular_function": {"count": 0, "name": ""},
            "biological_process": {"count": 0, "name": ""},
            "cellular_component": {"count": 0, "name": ""}
        }

    #   Called when a new tag starts
    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == "term":
            #   Reset term info
            self.current_namespace = ""
            self.current_name = ""
            self.current_is_a_count = 0
        elif tag == "is_a":
            self.current_is_a_count += 1

    #   Called when characters are read between tags
    def characters(self, content):
        if self.current_tag == "namespace":
            self.current_namespace += content
        elif self.current_tag == "name":
            self.current_name += content

    #   Called when a tag ends
    def endElement(self, tag):
        if tag == "term":
            #   Check if this term has the most <is_a> in its category
            if self.current_namespace in self.max_is_a:
                if self.current_is_a_count > self.max_is_a[self.current_namespace]["count"]:
                    self.max_is_a[self.current_namespace]["count"] = self.current_is_a_count
                    self.max_is_a[self.current_namespace]["name"] = self.current_name
        self.current_tag = ""

#   Define the function to run the SAX parser
def find_max_is_a_sax(filename):
    #   Start the timer
    start_time = time.time()

    #   Set up parser and handler
    parser = xml.sax.make_parser()
    handler = GOHandler()
    parser.setContentHandler(handler)

    #   Parse the file
    with open(filename, 'r', encoding='utf-8') as file:
        parser.parse(file)

    #   End the timer
    end_time = time.time()
    duration = end_time - start_time

    #   Print results for each ontology category
    print("\nSAX Method Results:")
    for key in handler.max_is_a:
        print(f"{key}:")
        print(f" Term with most <is_a>: {handler.max_is_a[key]['name']}")
        print(f" Number of <is_a>: {handler.max_is_a[key]['count']}\n")

    print(f"Time taken by SAX method: {duration:.4f} seconds")

    #   Return time for comparison with DOM
    return duration

#   Main program
def main():
    #   Set file name
    filename = "go_obo.xml"

    #   Run SAX method
    find_max_is_a_sax(filename)

#   Run the script
main()
#  Sax analysis method is faster than Dom