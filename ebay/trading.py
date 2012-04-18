from utils import get_endpoint_response, get_config_value
from lxml import etree
from xml.dom.minidom import parseString


def getCategories(parentId=None, \
                detailLevel='ReturnAll', \
                errorLanguage=None, \
                messageId=None, \
                outputSelector=None, \
                version=None, \
                warningLevel="High", \
                levelLimit=1, \
                viewAllNodes=True, \
                categorySiteId=0, \
                encoding="JSON"):
    """
    Using a query string and parentId this function returns
    all the categories containing that string within the category name,
    and as a subcategory of the category defined by the parentId.
    If the parentId is missing, it simply returns a list of all the
    top-level categories.
    (based on
    http://developer.ebay.com/DevZone/XML/docs/Reference/eBay/GetCategories.html#Request)
    """
    #get the user auth token
    token = get_config_value({("auth", "token"): "", })[("auth", "token")]

    root = etree.Element("GetCategoriesRequest",
                         xmlns="urn:ebay:apis:eBLBaseComponents")
    #add it to the xml doc
    credentials_elem = etree.SubElement(root, "RequesterCredentials")
    token_elem = etree.SubElement(credentials_elem, "eBayAuthToken")
    token_elem.text = token

    if parentId == None and levelLimit:
        levelLimit_elem = etree.SubElement(root, "LevelLimit")
        levelLimit_elem.text = str(levelLimit)
    elif parentId:
        parentId_elem = etree.SubElement(root, "CategoryParent")
        parentId_elem.text = str(parentId)

    viewAllNodes_elem = etree.SubElement(root, "ViewAllNodes")
    viewAllNodes_elem.text = str(viewAllNodes).lower()

    categorySiteId_elem = etree.SubElement(root, "CategorySiteID")
    categorySiteId_elem.text = str(categorySiteId)

    if detailLevel:
        detailLevel_elem = etree.SubElement(root, "DetailLevel")
        detailLevel_elem.text = detailLevel

    if errorLanguage:
        errorLanguage_elem = etree.SubElement(root, "ErrorLanguage")
        errorLanguage_elem.text = errorLanguage

    if messageId:
        messageId_elem = etree.SubElement(root, "MessageID")
        messageId_elem.text = messageId

    if outputSelector:
        outputSelector_elem = etree.SubElement(root, "OutputSelector")
        outputSelector_elem.text = outputSelector

    if version:
        version_elem = etree.SubElement(root, "Version")
        version_elem.text = version

    if warningLevel:
        warningLevel_elem = etree.SubElement(root, "WarningLevel")
        warningLevel_elem.text = warningLevel

    #need to specify xml declaration and encoding or else will get error
    request = etree.tostring(root, pretty_print=False,
                              xml_declaration=True, encoding="utf-8")
    response = get_response("GetCategories", request, encoding)

    return response


def _get_single_value(node, tag):
    nl = node.getElementsByTagName(tag)
    if len(nl) > 0:
        tagNode = nl[0]
        if tagNode.hasChildNodes():
            return tagNode.firstChild.nodeValue
    return -1


def filterCategories(xml_data, query=''):
    to_return = []  # TODO: in future would be cool if categories were objects
    if xml_data:
        categoryList = parseString(xml_data)
        catNodes = categoryList.getElementsByTagName("Category")
        for node in catNodes:
            addNode = False  # assume it's not being added
            if query:
                lquery = query.lower()
                name = _get_single_value(node, "CategoryName")
                if name.lower().find(lquery) != -1:
                    addNode = True  # name contains our query, will add it
            else:
                addNode = True  # no filter given, add all
            if addNode:
                # add node to the list if we need to
                to_return.append(node.toxml())

    return to_return


def get_response(operation_name, data, encoding, **headers):
    return get_endpoint_response("trading", operation_name,
                                  data, encoding, **headers)
