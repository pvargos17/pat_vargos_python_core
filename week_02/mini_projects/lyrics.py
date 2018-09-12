'''
--------------------------------------------------------
                PROGRAMMED SONG LYRICS
--------------------------------------------------------

Programmatically create your own song lyrics with multiple verses,
interlaced with a repeating chorus.

- use one block of text as verse input (hint: linebreaks can be helpful!)
- use a for loop for creating the full lyrics


'''

# I cheated, i cant come up with lyrics Stole this from the beatles.

lyrics = """ When I find myself in times of trouble, Mother Mary comes to me

And in my hour of darkness she is standing right in front of me"""

chorus = "Speaking words of wisdom, let it be"

verse = lyrics.split("\n\n")  # split the lyrics on two newlines


for v in verse:
    print(v)
    print((chorus + "\n") * 2)


