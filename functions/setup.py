#	Author: Sean Lobo
#	Date: Feb 16, 2016
#	File Purpose: Trying to improve composition of project
#				  and consolidate functions

from bs4 import BeautifulSoup


def get_all_divs(msg_html_path):
    """Returns a list of list of divs. Contains all information
    needed to get full conversation history for any conversation.

    Return type has the following structure:

    [[msg_div1, msg_div2, msg_div3],
     [msg_div1],
     [msg_div1, msg_div2, msg_div3, msg_div4]
     .
     .
     .
    ]

    each inner list has an arbitrary length. The elemens of each
    inner list are div tags that contain 1 thread each

    A thread is a list of up to 10,000 messages between two people
    or one group. The conversation the thread belongs to can be
    found by:

    thread.contents[0]
    """
    try:
        text = open(msg_html_path, mode='r', encoding='UTF8')
    except OSError as err:
        print('OS error: {0}'.format(err))
        exit()

    # soup object that holds all of the html
    soup = BeautifulSoup(text, 'html.parser')
    # finds the outer div tag that holds all relevant information
    divs = []
    for div in soup.find_all('div', class_='contents'):
        divs.append(div)
    div_tag = divs[0]

    footer = []
    for foot in soup('div', class_='footer'):
        footer.append(foot)

    divs = None
    soup = None

    # creates a list containing elements whose div
    # tags hold the chat data
    all_divs = [] # list of list of divs [ [div, div], [div], ...]
    for div in div_tag("div", recursive=False):
        all_divs.append(div)

    return (all_divs, footer[0].contents[0])

def get_convo_divs(all_divs, convo_name=None):
    """Returns a list of message_divs (threads) whose contents
    match the passed convo_name, or all message_divs by default

    Return type has the following sturcture:

    [thread1,
    thread2,
    thread3,
    .
    .
    .
    ]
    """
    all_divs, footer = all_divs

    def contents_equal(lst1, lst2):
        if len(lst1) != len(lst2):
            return False
        for ele in lst1:
            if ele not in lst2:
                return False
        return True

    if convo_name is not None:
        assert type(convo_name) is list, "You must pass in a list \
                                          of names"

    bucket = []
    for msg_container in all_divs:
        for msg_div in msg_container('div', class_="thread", recursive=False):
            person = msg_div.contents[0].split(', ')
            if convo_name is None or contents_equal(person, convo_name):
                bucket.append(msg_div)

    return (bucket, footer)


def get_messages_readable(thread, previous=None):
    """Returns a list of tuples of length 3. First element is person speaking,
    second message, third time
    """
    if previous is None:
        previous = []

    # list of all div ids for a certain message group
    # (each message group has max 10,000 messages)
    # each element (div id tag) has the time and person of the message
    div_ids = [div for div in thread('div', class_='message', recursive=False)]
    # a list of messages. Each element corresponds to the information in div_ids
    messages = [p for p in thread('p', recursive=False)]
    assert len(div_ids) == len(messages), 'div_ids and messages\
                                             have different lengths'

    for i in range(len(div_ids) - 1, -1, -1):
        # person who said the ith message
        person = [div for div in div_ids[i]('span', class_='user')][0].contents[0]
        # time ith message was sent at
        time = [div for div in div_ids[i]('span', class_='meta')][0].contents[0]

        try:
            msg = messages[i].get_text()
        except IndexError:
            msg = ''
        previous.append( (person, msg, time) )

    return previous


def get_all_msgs_dict(msg_html_path='./messages.htm'):
    all_divs = get_all_divs(msg_html_path)

    convo_divs, footer = get_convo_divs(all_divs)

    msgs = dict()
    for thread in convo_divs:
        convo_name = thread.contents[0]
        if convo_name in msgs:
            msgs[convo_name].extend(get_messages_readable(thread))
        else:
            msgs[convo_name] = get_messages_readable(thread)

    print('\a', '')
    return (msgs, str(footer))


