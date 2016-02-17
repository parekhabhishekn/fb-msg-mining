# Facebook Chat Data Analyzer

## Installing dependencies

To install dependencies run:

    pip3 install -r requirements.txt


## Step 1:

Request a copy of your Facebook data

Settings -> "Download a copy" link near the bottom of page


## Step 2:

Use the link emailed to you by facebook to download a copy of your data


## Step 3:

Extract the zip you get and put `html/messages.htm` in a location you have access to


## Step 4:

Rename `paths.txt.examples` --> `paths.txt`


## Step 5:

Add the absolute path to `html/messages.htm` to `paths.txt`

Add the absolute path to `data.txt`, the location where chat data will be stored, to `paths.txt`


## Step 6:

Run `main.py`


## Using Fb-msg-mining

After setup is complete, run `python3 -i test.py`

You start with a MessageReader object stored in the variable m, which holds all your chat history for all contacts.

Example uses of methods

```python
### MessageReader class ###
m.print_names() # prints to the screen your contacts in decreasing order of chatted frequency
 # 1) Most chatted
 # 2) Second most common
 # 3) etc.

nth_convo = m.get_convo(n) # returns the nth conversation, where n referres to the output of m.print_names()
```

### ConvoReader class ###

| Method   | Description |
|-------------|-------------|
|print_people( ) | Prints to the screen an alphabetically sorted list of people in the conversation |
|messages(name=None) | Returns either the number of messages spoken by the specified person, or if no name is passed, a Counter object storing the number of mesages as values paired with names of people as keys for all people in the chat |
|ave_words(name=None) | Returns either the average number of words spoken per message by the specified person, or if no name is passed, a Counter object storing the average number of words per message as values paired with names of people as keys
|frequency(person=None, word=None) | Returns either the average number of words spoken per message by the specified person, or if no name is passed, a Counter object storing the average number of words per message as values paired with names of people as keys.
| prettify( ) | Returns a string that \"prettily\" shows the conversation history |
| msgs_graph(contact=None) | Returns a list of length 2 lists that store a day as element 0 and the number of total messages sent that day as element 1 |
| print_msgs_graph(contact=None) | Prettily prints to the screen the message history of a chat |
| msgs_by_weekday( ) | Returns a list containing frequency of chatting by days of week, ordered by index, with 0 being Monday and 6 Sunday |
| msgs_by_day(window=60, contact=None) | Returns a list containing average frequency of chatting by times in days, starting at 12:00 am. Default window is 60 minute interval.If time less than the passed window is left at the end, it is put at the end of the list |
| print_msgs_by_day(window=60, threshold=None, contact=None) | Prints to the screen a graphical result of msgs_by_day |
| save_word_freq( ) | Saves to a file the ordered rankings of word frequencies by person in the chat |




