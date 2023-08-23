from collections import Counter
def ransom_note_possible(magazine,ransom_note):
    magazine    = magazine.replace(" ","")
    ransom_note = ransom_note.replace(" ","")

    c_magazine      = Counter(magazine)
    c_ransom_note   = Counter(ransom_note)

    for key in c_ransom_note.keys():
        if key in c_ransom_note and c_ransom_note[key] <= c_magazine[key]:
            continue
        else:
            return False
    return True


magazine = "Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph. A paragraph is defined as a group of sentences or a single sentence that forms a unit (Lunsford and Connors 116). Length and appearance do not determine whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly journalistic styles, a paragraph can be just one sentence long. Ultimately, a paragraph is a sentence or group of sentences that support one main idea. In this handout, we will refer to this as the controlling idea, because it controls what happens in the rest of the paragraph."
ransom_note = "In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph"
print(ransom_note_possible(magazine,ransom_note))