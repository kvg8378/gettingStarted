def welcome_assignment_answers(question):
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"

    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"

    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"

    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"

    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"

    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = "4b3f6b6c66e2b7c7b8f0c3b3a6f0a28b0c5bb5f8a9a9c35cdbd22fc8c9e1a0cf"

    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"

    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = 5  

    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = 3  

    else:
        answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
    return answer


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))
