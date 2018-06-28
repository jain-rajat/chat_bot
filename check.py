import re
import random
pairs = (

  (r'I need (.*) book',
  ( "Press /book to book a table",
    "Press /help"
    )),

    (r'I nekk4ed (.*) book',
  ( "Press /boesfok to book a table",
    "Press /helfefp %1"
    ))

  )


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

pair = [(re.compile(x, re.IGNORECASE),y) for (x,y) in pairs]
for x,y in pair:
	z=x.match('I need hello book')
	print(z)
	print(random.choice(y))
	print(z.group(1))
	break
sorted_refl = sorted(reflections.keys(), key=len,
                reverse=True)
print(sorted_refl)



r=re.compile(r"\b({0})\b".format("|".join(map(re.escape,
            sorted_refl))), re.IGNORECASE)

r.sub(lambda mo:
                self._reflections[mo.string[mo.start():mo.end()]],
                    "hello")

print()

print(r)
