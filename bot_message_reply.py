#from __future__ import print_function

import re
import random

#from six.moves import input


reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

class Chat(object):
    def __init__(self, pairs, reflections={}):

        self._pairs = [(re.compile(x, re.IGNORECASE),y) for (x,y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()


    def _compile_reflections(self):
        sorted_refl = sorted(self._reflections.keys(), key=len,
                reverse=True)
        return  re.compile(r"\b({0})\b".format("|".join(map(re.escape,
            sorted_refl))), re.IGNORECASE)

    def _substitute(self, str):

        print(mo)
        return self._regex.sub(lambda mo:
                self._reflections[mo.string[mo.start():mo.end()]],
                    str.lower())

    def _wildcards(self, response, match):
        pos = response.find('%')
        while pos >= 0:
            num = int(response[pos+1:pos+2])
            print(match.group(num))
            response = response[:pos] + \
                self._substitute(match.group(num)) + \
                response[pos+2:]
            pos = response.find('%')
        return response

    def respond(self, str):

        for (pattern, response) in self._pairs:
            print(pattern)
            match = pattern.match(str)

            
            if match:
                resp = random.choice(response) 
                print(resp)
                resp = self._wildcards(resp, match) 

          
                if resp[-2:] == '?.': resp = resp[:-2] + '.'
                if resp[-2:] == '??': resp = resp[:-2] + '?'
                return resp


 


pairs = (

  (r'I need (.*) book',
  ( "Press /book to book a table",
    "Press /help"
    )),

  (r'I can\'t (.*) book',
  ( "I am sorry! Try again later or call us at +91-98989",
    "Apologies. Try again by press /book")),

  (r'I am (.*)',
  ( "Did you come to me because you are %1?",
    "How long have you been %1?",
    "How do you feel about being %1?")),

  (r'I\'m (.*)',
  ( "How does being %1 make you feel?",
    "Do you enjoy being %1?",
    "Why do you tell me you're %1?",
    "Why do you think you're %1?")),

  (r'Are you (.*)',
  ( "Why does it matter whether I am %1?",
    "Would you prefer it if I were not %1?",
    "Perhaps you believe I am %1.",
    "I may be %1 -- what do you think?")),

  (r'What (.*)',
  ( "Why do you ask?",
    "How would an answer to that help you?",
    "What do you think?")),

  
  (r'Because (.*)',
  ( "Is that the real reason?",
    "What other reasons come to mind?",
    "Does that reason apply to anything else?",
    "If %1, what else must be true?")),

  (r'(.*) sorry (.*)',
  ( "There are many times when no apology is needed.",
    "What feelings do you have when you apologize?")),

  (r'Hello(.*)',
  ( "Hello... I'm glad you could drop by today.",
    "Hi there... how are you today?",
    "Hello, how are you feeling today?")),


  (r'Hi(.*)',
  ( "Hello... I'm glad you could drop by today.",
    "Hi there... how are you today?",
    "Hello, how are you feeling today?")),

  (r'What\'s up(.*)',
  ( "Hello... I'm glad you could drop by today.",
    "Hi there... how are you today?",
    "Hello, how are you feeling today?")),

  (r'Hey(.*)',
  ( "Hello... I'm glad you could drop by today.",
    "Hi there... how are you today?",
    "Hello, how are you feeling today?")),

  (r'I think (.*)',
  ( "Do you doubt %1?",
    "Do you really think so?",
    "But you're not sure %1?")),

  (r'Yes',
  ( "You seem quite sure.",
    "OK, but can you elaborate a bit?")),

  (r'(.*)book(.*)',
  ( "If you want to book a table press or type /book","Yes I ham here to book a table. Press /book to book or /details to see your booking")),



  (r'(.*) computer(.*)',
  ( "Are you really talking about me?",
    "Does it seem strange to talk to a computer?",
    "How do computers make you feel?",
    "Do you feel threatened by computers?")),

  (r'Is it (.*)',
  ( "Do you think it is %1?",
    "Perhaps it's %1 -- what do you think?",
    "If it were %1, what would you do?",
    "It could well be that %1.")),

  (r'Can you (.*) book',
  ( "Press /book",
    "Press /help")),

  (r'Can I (.*) book',
  ( "Yes! Press /book",
    "Press /help")),

  (r'You are (.*)',
  ( "Why do you think I am %1?",
    "Does it please you to think that I'm %1?",
    "Perhaps you would like me to be %1.",
    "Perhaps you're really talking about yourself?")),

  (r'You\'re (.*)',
  ( "Why do you say I am %1?",
    "Why do you think I am %1?",
    "Are we talking about you, or me?")),

  (r'I don\'t (.*)',
  ( "Don't you really %1?",
    "Why don't you %1?",
    "Do you want to %1?")),

  (r'I feel (.*)',
  ( "Good, tell me more about these feelings.",
    "Do you often feel %1?",
    "When do you usually feel %1?",
    "When you feel %1, what do you do?")),

  (r'I have (.*)',
  ( "Why do you tell me that you've %1?",
    "Have you really %1?",
    "Now that you have %1, what will you do next?")),

  (r'I would (.*)book',
  ( "Press /book to book",
    "Press /help")),

  (r'My (.*)',
  ( "I see, your %1.",
    "Why do you say that your %1?",
    "When your %1, how do you feel?")),

  (r'You (.*)',
  ( "We should be discussing you, not me.",
    "Why do you say that about me?",
    "Why do you care whether I %1?")),

  (r'Why (.*)',
  ( "Why don't you tell me the reason why %1?",
    "Why do you think %1?" )),

  (r'I want (.*)',
  ( "What would it mean to you if you got %1?",
    "Why do you want %1?",
    "What would you do if you got %1?",
    "If you got %1, then what would you do?")),


  (r'(.*)',
  ( "I am sorry I didn't get you! Press /help for information","Press /help for more information"
    ))
  
)


c=Chat(pairs)
def result(text):
    return c.respond(text)





