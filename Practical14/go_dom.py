#   Import required modules
import xml.dom.minidom
import time

#   Define the function to process the XML file using DOM
def find_max_is_a_dom(filename):
    #   Start the timer
    start_time = time.time()

    #   Load and parse the XML file
    dom_tree = xml.dom.minidom.parse(filename)
    root = dom_tree.documentElement

    #   Get all <term> elements
    terms = root.getElementsByTagName("term")

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

#   Main program
def main():
    #   Set the XML file name
    filename = "go_obo.xml"

    #   Run the DOM parser
    find_max_is_a_dom(filename)

#   Run the program
main()
