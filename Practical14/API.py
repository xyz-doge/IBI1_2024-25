#   Import required modules
import xml.dom.minidom
import xml.sax
import time

#   Define the function to process the XML file using DOM
def find_max_is_a_dom(filename):
    #   Start the timer
    start_time = time.time()

    #   Load and parse the XML file
    dom_tree = xml.dom.minidom.parse(filename)

    #   Get all <term> elements
    terms = dom_tree.getElementsByTagName("term")

    #   Prepare dictionary to record max is_a counts for each ontology
    max_is_a = {
        "molecular_function": {"count": 0, "name": ""},
        "biological_process": {"count": 0, "name": ""},
        "cellular_component": {"count": 0, "name": ""}
    }

    #   Loop through each <term> element
    for term in terms:
        #   Get the <namespace> text
        ns = term.getElementsByTagName("namespace")[0].firstChild.nodeValue

        #   Get the <name> text (check if it exists)
        name_tag = term.getElementsByTagName("name")
        if name_tag and name_tag[0].firstChild:
            name = name_tag[0].firstChild.nodeValue
        else:
            name = "Unknown"

        #   Count how many <is_a> tags are present
        is_as = term.getElementsByTagName("is_a")
        is_a_count = len(is_as)

        #   If this is the largest count so far in its category, update the record
        if ns in max_is_a and is_a_count > max_is_a[ns]["count"]:
            max_is_a[ns]["count"] = is_a_count
            max_is_a[ns]["name"] = name

    #   End the timer and calculate time spent
    end_time = time.time()
    duration = end_time - start_time

    #   Print results for each ontology category
    print("\nDOM Method Results:")
    for key in max_is_a:
        print(f"{key}:")
        print(f" Term with most <is_a>: {max_is_a[key]['name']}")
        print(f" Number of <is_a>: {max_is_a[key]['count']}\n")

    #   Print total time used
    print(f"Time taken by DOM method: {duration:.4f} seconds")

    #   Return time for later comparison with SAX
    return duration

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
    #   Set the XML file name
    filename = "go_obo.xml"

    #   Run both methods
    dom_time = find_max_is_a_dom(filename)
    sax_time = find_max_is_a_sax(filename)

    #   Compare time (optional)
    print(f"\nComparison: SAX is {'faster' if sax_time < dom_time else 'slower'} than DOM by {abs(dom_time - sax_time):.4f} seconds.")

#   Run the program
main()
#  Sax analysis method is faster than Dom