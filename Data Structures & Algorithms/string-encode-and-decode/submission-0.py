class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for seq in strs:
            length = f"{len(seq)}"
            length = length.rjust(3, "0")
            encoded +=  f'{length}{seq}'
        return encoded

    def decode(self, s: str) -> List[str]:
        def extract_elements(s: str, extracted: List[str]):
            if s == "":
                return extracted
            length = int(s[:3])
            extracted.append(s[3:length+3])
            return extract_elements(s[length+3:], extracted)
        return extract_elements(s, [])
        

