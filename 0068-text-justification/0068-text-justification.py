class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result  = []
        i = 0

        while i < len(words):
            line_words = []
            line_length = 0

            while i < len(words):
                needed_length = line_length + len(words[i]) + len(line_words)
                if needed_length > maxWidth:
                    break
                
                line_words.append(words[i])
                line_length += len(words[i])
                i += 1
            
            justified_line = self.justify_line(line_words, maxWidth, i == len(words))
            result.append(justified_line)
        
        return result

    def justify_line(self, words, maxWidth, is_last_line):
        if len(words) == 1 or is_last_line:
        # Single word or last line: left-justify
            line = ' '.join(words)
            return line + ' ' * (maxWidth - len(line))
    
        # Calculate spaces to distribute
        total_word_length = sum(len(word) for word in words)
        total_spaces = maxWidth - total_word_length
        gaps = len(words) - 1
        
        # Distribute spaces evenly, with extra spaces going to leftmost gaps
        spaces_per_gap = total_spaces // gaps
        extra_spaces = total_spaces % gaps
        
        # Build the justified line
        result = []
        for i in range(len(words)):
            result.append(words[i])
            
            # Add spaces after each word except the last
            if i < len(words) - 1:
                spaces = spaces_per_gap
                # Add extra space if this is one of the leftmost gaps
                if i < extra_spaces:
                    spaces += 1
                result.append(' ' * spaces)
        
        return ''.join(result)