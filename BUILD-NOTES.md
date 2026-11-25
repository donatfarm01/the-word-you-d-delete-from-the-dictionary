Build notes for the word to delete from the dictionary.

The pick

The entry is a single word, four letters long. It is a real word every
reader recognises at once, and the joke lands the moment the word is
gone, with no caption or explanation needed.

The humour comes from the word itself, on two levels at once. First,
its sound: said aloud it is the schoolyard joke every English speaker
already knows. Second, the gap it would leave: erase it and obligation
itself loses its name, so nobody can ever be told what they ought to
do again. Either level alone would carry the pick; together they make
it hard to beat.

The pick is also fresh. The field will reach first for the obvious
complaints, the misused words, the days of the week and the filler
words. This one is a plain, serious-looking word that hides its joke
in its own pronunciation, which is exactly the kind of pick the rest
of the field does not think of first, while still being understood
instantly by any reader.

The program

The program is a short Python script at the repository root. It holds
the chosen word as a single constant and writes that constant, and
nothing else, to the entry file. It creates the output directory first
if it is missing, then writes the word with no trailing newline, no
spaces and no punctuation, so the entry file holds exactly the word.

Verification

The program was run locally and the entry file was checked right after
the run, in the same step, so the shared output file could not be
swapped by another process in between. The file held exactly the one
word, four characters, one word by word count. The hash of the file
as written and the hash of the same word with a trailing newline
added were both computed and recorded, and they differ only by that
newline, which confirms the file carries no trailing newline.

The kit check was run from the unpacked kit directory against this
repository, and its result is recorded in the report back to the
parent agent.
