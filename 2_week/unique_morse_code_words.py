from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        result_set = set()
        for word in words:
            result_string = ''
            for letter in word:
                result_string += morse_code[ord(letter) - ord('a')]
            result_set.add(result_string)
        return len(result_set)
