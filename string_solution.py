"""
SafeString - A security-focused string class for protocol handling
Complete implementation for all base code functions
"""

class SafeStringError(Exception):
    """Base exception for SafeString errors"""
    pass

class BufferOverflowError(SafeStringError):
    """Raised when operation would exceed buffer capacity"""
    pass

class InvalidCharacterError(SafeStringError):
    """Raised when non-ASCII character is encountered"""
    pass

class IndexOutOfBoundsError(SafeStringError):
    """Raised when accessing out of bounds index"""
    pass


class SafeString:
    """
    A security-focused string class with fixed capacity and ASCII validation.
    
    This class is designed for handling protocol strings where buffer size
    and character encoding must be strictly controlled.
    """
    
    def __init__(self, capacity: int, initial_value: str = ""):
        """
        Initialize SafeString with fixed capacity.
        
        Args:
            capacity: Maximum number of characters (fixed buffer size)
            initial_value: Initial string content (optional)
            
        Raises:
            BufferOverflowError: If initial_value exceeds capacity
            InvalidCharacterError: If initial_value contains non-ASCII characters
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
            
        self._capacity = capacity
        self._buffer = ['\0'] * capacity
        self._length = 0
        
        if initial_value:
            self.assign(initial_value)
    
    def __len__(self) -> int:
        """Return current length of the string."""
        return self._length
    
    @property
    def capacity(self) -> int:
        """Return maximum capacity of the string."""
        return self._capacity
    
    def __str__(self) -> str:
        """Return Python string representation."""
        return ''.join(self._buffer[:self._length])
    
    def __repr__(self) -> str:
        """Return detailed representation for debugging."""
        return f"SafeString(capacity={self._capacity}, value='{self}')"
    
    def clear(self) -> None:
        """Clear the string content."""
        self._buffer = ['\0'] * self._capacity
        self._length = 0
    
    def is_ascii(self, text: str) -> bool:
        """
        Check if all characters in text are valid ASCII.
        
        Args:
            text: String to validate
            
        Returns:
            True if all characters are ASCII (0-127), False otherwise
        """
        try:
            # Check each character's ordinal value is in ASCII range
            for char in text:
                if not (0 <= ord(char) <= 127):
                    return False
            return True
        except TypeError:
            # If text is not a string or iterable
            return False
    
    def assign(self, text: str) -> None:
        """
        Assign new content to the string.
        
        Args:
            text: New string content
            
        Raises:
            BufferOverflowError: If text length exceeds capacity
            InvalidCharacterError: If text contains non-ASCII characters
        """
        # 1. Validate text length doesn't exceed capacity
        if len(text) > self._capacity:
            raise BufferOverflowError(f"Text length {len(text)} exceeds capacity {self._capacity}")
        
        # 2. Validate text contains only ASCII characters
        if not self.is_ascii(text):
            raise InvalidCharacterError("Text contains non-ASCII characters")
        
        # 3. Clear current buffer
        self.clear()
        
        # 4. Copy text to buffer
        for i, char in enumerate(text):
            self._buffer[i] = char
        
        # 5. Update length
        self._length = len(text)
    
    def append(self, text: str) -> None:
        """
        Append text to the end of the string.
        
        Args:
            text: Text to append
            
        Raises:
            BufferOverflowError: If combined length exceeds capacity
            InvalidCharacterError: If text contains non-ASCII characters
        """
        # 1. Validate text contains only ASCII characters
        if not self.is_ascii(text):
            raise InvalidCharacterError("Text contains non-ASCII characters")
        
        # 2. Check if combined length would exceed capacity
        new_length = self._length + len(text)
        if new_length > self._capacity:
            raise BufferOverflowError(f"Appending would exceed capacity {self._capacity}")
        
        # 3. If safe, append text to buffer
        for i, char in enumerate(text):
            self._buffer[self._length + i] = char
        
        # 4. Update length
        self._length = new_length
    
    def append_char(self, char: str) -> None:
        """
        Append a single character to the string.
        
        Args:
            char: Single character to append
            
        Raises:
            BufferOverflowError: If string is at capacity
            InvalidCharacterError: If char is not ASCII
            ValueError: If char is not a single character
        """
        # 1. Validate char is a single character
        if len(char) != 1:
            raise ValueError(f"Expected single character, got string of length {len(char)}")
        
        # 2. Validate char is ASCII
        if not self.is_ascii(char):
            raise InvalidCharacterError(f"Character '{char}' is not ASCII")
        
        # 3. Check if there's space
        if self._length >= self._capacity:
            raise BufferOverflowError(f"Cannot append character, at capacity {self._capacity}")
        
        # 4. Append to buffer and update length
        self._buffer[self._length] = char
        self._length += 1
    
    def find(self, substring: str) -> int:
        """
        Find first occurrence of substring.
        
        Args:
            substring: Substring to search for
            
        Returns:
            Index of first occurrence, or -1 if not found
            
        Raises:
            InvalidCharacterError: If substring contains non-ASCII characters
        """
        # 1. Validate substring is ASCII
        if not self.is_ascii(substring):
            raise InvalidCharacterError("Substring contains non-ASCII characters")
        
        # 2. Search for substring in buffer
        # Convert to string for easier searching
        current_str = str(self)
        return current_str.find(substring)
    
    def substr(self, start: int, length: int = None) -> 'SafeString':
        """
        Extract substring as a new SafeString.
        
        Args:
            start: Starting index
            length: Number of characters (default: to end of string)
            
        Returns:
            New SafeString containing the substring
            
        Raises:
            IndexOutOfBoundsError: If start is out of bounds
        """
        # 1. Validate start index
        if start < 0 or start >= self._length:
            raise IndexOutOfBoundsError(f"Start index {start} out of bounds (length {self._length})")
        
        # 2. Calculate actual length (min of requested and available)
        if length is None:
            # Default to remaining characters
            actual_length = self._length - start
        else:
            # Ensure we don't go beyond the end
            actual_length = min(length, self._length - start)
        
        # 3. Create new SafeString with appropriate capacity
        # Use same capacity as original for consistency
        result = SafeString(self._capacity)
        
        # 4. Copy substring to new SafeString
        for i in range(actual_length):
            result._buffer[i] = self._buffer[start + i]
        result._length = actual_length
        
        return result
    
    def at(self, index: int) -> str:
        """
        Safely get character at index.
        
        Args:
            index: Character position
            
        Returns:
            Character at index
            
        Raises:
            IndexOutOfBoundsError: If index is out of bounds
        """
        # 1. Validate index is within bounds
        if index < 0 or index >= self._length:
            raise IndexOutOfBoundsError(f"Index {index} out of bounds (length {self._length})")
        
        # 2. Return character from buffer
        return self._buffer[index]
    
    def __getitem__(self, index: int) -> str:
        """Support indexing with bounds checking."""
        return self.at(index)
    
    def __eq__(self, other: object) -> bool:
        """
        Compare two SafeStrings for equality.
        
        Args:
            other: Another SafeString or string
            
        Returns:
            True if contents are equal, False otherwise
        """
        # 1. Handle comparison with SafeString objects
        if isinstance(other, SafeString):
            # Quick length check
            if self._length != other._length:
                return False
            
            # Compare character by character
            for i in range(self._length):
                if self._buffer[i] != other._buffer[i]:
                    return False
            return True
        
        # 2. Handle comparison with Python strings
        elif isinstance(other, str):
            # Quick length check
            if self._length != len(other):
                return False
            
            # Compare character by character
            for i in range(self._length):
                if self._buffer[i] != other[i]:
                    return False
            return True
        
        # 3. Return False for other types
        return False
    
    def __add__(self, other: 'SafeString') -> 'SafeString':
        """
        Concatenate two SafeStrings.
        
        Args:
            other: Another SafeString to concatenate
            
        Returns:
            New SafeString containing concatenated result
            
        Raises:
            BufferOverflowError: If combined length exceeds capacity of result
        """
        # 1. Calculate combined length
        combined_length = self._length + other._length
        
        # 2. Create new SafeString with capacity = max(self.capacity, other.capacity)
        result_capacity = max(self._capacity, other._capacity)
        
        # Check if combined length fits
        if combined_length > result_capacity:
            raise BufferOverflowError(
                f"Concatenated length {combined_length} exceeds capacity {result_capacity}"
            )
        
        result = SafeString(result_capacity)
        
        # 3. Copy self then other
        # Copy self
        for i in range(self._length):
            result._buffer[i] = self._buffer[i]
        
        # Copy other
        for i in range(other._length):
            result._buffer[self._length + i] = other._buffer[i]
        
        result._length = combined_length
        
        # 4. Return new SafeString
        return result
    
    def starts_with(self, prefix: str) -> bool:
        """
        Check if string starts with prefix.
        
        Args:
            prefix: Prefix to check
            
        Returns:
            True if string starts with prefix, False otherwise
            
        Raises:
            InvalidCharacterError: If prefix contains non-ASCII characters
        """
        # 1. Validate prefix is ASCII
        if not self.is_ascii(prefix):
            raise InvalidCharacterError("Prefix contains non-ASCII characters")
        
        # 2. Check if prefix length <= self._length
        prefix_len = len(prefix)
        if prefix_len > self._length:
            return False
        
        # 3. Compare characters
        for i in range(prefix_len):
            if self._buffer[i] != prefix[i]:
                return False
        
        return True
    
    def ends_with(self, suffix: str) -> bool:
        """
        Check if string ends with suffix.
        
        Args:
            suffix: Suffix to check
            
        Returns:
            True if string ends with suffix, False otherwise
            
        Raises:
            InvalidCharacterError: If suffix contains non-ASCII characters
        """
        # 1. Validate suffix is ASCII
        if not self.is_ascii(suffix):
            raise InvalidCharacterError("Suffix contains non-ASCII characters")
        
        # 2. Check if suffix length <= self._length
        suffix_len = len(suffix)
        if suffix_len > self._length:
            return False
        
        # 3. Compare characters from the end
        start_index = self._length - suffix_len
        for i in range(suffix_len):
            if self._buffer[start_index + i] != suffix[i]:
                return False
        
        return True
    
    def replace(self, old: str, new: str) -> 'SafeString':
        """
        Replace all occurrences of old substring with new.
        
        Args:
            old: Substring to replace
            new: Replacement substring
            
        Returns:
            New SafeString with replacements
            
        Raises:
            InvalidCharacterError: If old or new contains non-ASCII
            BufferOverflowError: If replacement would exceed capacity
        """
        # 1. Validate both strings are ASCII
        if not self.is_ascii(old):
            raise InvalidCharacterError("Old substring contains non-ASCII characters")
        if not self.is_ascii(new):
            raise InvalidCharacterError("New substring contains non-ASCII characters")
        
        # 2. Create new SafeString with same capacity
        result = SafeString(self._capacity)
        
        # 3. Perform replacement
        # Convert to string for easier replacement
        current_str = str(self)
        replaced_str = current_str.replace(old, new)
        
        # 4. Check length doesn't exceed capacity
        if len(replaced_str) > self._capacity:
            raise BufferOverflowError(
                f"Replacement would result in length {len(replaced_str)} exceeding capacity {self._capacity}"
            )
        
        # Assign the replaced string
        if replaced_str:
            result.assign(replaced_str)
        
        # 5. Return new SafeString
        return result
