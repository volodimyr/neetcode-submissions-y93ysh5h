class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2:
            return len(chars)
        read = 0
        write = 0
        while read < len(chars):
            group = read
            while group < len(chars) and chars[group] == chars[read]:
                group+=1
            if group - read > 1:
                for c in chars[read] + str(group-read):
                    chars[write] = c
                    write+=1
            else:
                chars[write] = chars[read]
                write+=1
            read = group
        return write