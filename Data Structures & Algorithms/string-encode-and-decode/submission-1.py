class Solution:

    def encode(self, strs: List[str]) -> str:

        str2 =""
        for word in strs:
            str2+=str(len(word))+"#"+word
        print(str2)
     

        return str2

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # Step 1: walk forward from i until we hit '#', collecting digits
            j = i
            length_str = ""
            while s[j] != "#":
                length_str += s[j]
                j += 1
            # now s[j] is '#', and length_str holds the number as text
            length = int(length_str)

            # Step 2: the actual word starts right after the '#'
            word_start = j + 1
            word = s[word_start : word_start + length]
            result.append(word)

            # Step 3: move i past this word, to the start of the next length-prefix
            i = word_start + length

        return result