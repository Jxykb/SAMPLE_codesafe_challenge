"""
SafeString - A security-focused string class for protocol handling
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
        TODO: Check if all characters in text are valid ASCII.
        
        Args:
            text: String to validate
            
        Returns:
            True if all characters are ASCII (0-127), False otherwise
        """
        # Implement ASCII validation
        # Return True if all characters have ordinal values 0-127
        # Return False otherwise
    
    def assign(self, text: str) -> None:
        """
        TODO: Assign new content to the string.
        
        Args:
            text: New string content
            
        Raises:
            BufferOverflowError: If text length exceeds capacity
            InvalidCharacterError: If text contains non-ASCII characters
        """
        # 1. Validate text length doesn't exceed capacity
        # 2. Validate text contains only ASCII characters
        # 3. Clear current buffer
        # 4. Copy text to buffer
        # 5. Update length
    
    def append(self, text: str) -> None:
        """
        TODO: Append text to the end of the string.
        
        Args:
            text: Text to append
            
        Raises:
            BufferOverflowError: If combined length exceeds capacity
            InvalidCharacterError: If text contains non-ASCII characters
        """
        # 1. Validate text contains only ASCII characters
        # 2. Check if combined length would exceed capacity
        # 3. If safe, append text to buffer
        # 4. Update length
    
    def append_char(self, char: str) -> None:
        """
        TODO: Append a single character to the string.
        
        Args:
            char: Single character to append
            
        Raises:
            BufferOverflowError: If string is at capacity
            InvalidCharacterError: If char is not ASCII
            ValueError: If char is not a single character
        """
        # 1. Validate char is a single character
        # 2. Validate char is ASCII
        # 3. Check if there's space
        # 4. Append to buffer and update length
    
    def find(self, substring: str) -> int:
        """
        TODO: Find first occurrence of substring.
        
        Args:
            substring: Substring to search for
            
        Returns:
            Index of first occurrence, or -1 if not found
            
        Raises:
            InvalidCharacterError: If substring contains non-ASCII characters
        """
        # 1. Validate substring is ASCII
        # 2. Search for substring in buffer
        # 3. Return index or -1
    
    def substr(self, start: int, length: int = None) -> 'SafeString':
        """
        TODO: Extract substring as a new SafeString.
        
        Args:
            start: Starting index
            length: Number of characters (default: to end of string)
            
        Returns:
            New SafeString containing the substring
            
        Raises:
            IndexOutOfBoundsError: If start is out of bounds
        """
        # 1. Validate start index
        # 2. Calculate actual length (min of requested and available)
        # 3. Create new SafeString with appropriate capacity
        # 4. Copy substring to new SafeString
    
    def at(self, index: int) -> str:
        """
        TODO: Safely get character at index.
        
        Args:
            index: Character position
            
        Returns:
            Character at index
            
        Raises:
            IndexOutOfBoundsError: If index is out of bounds
        """
        # 1. Validate index is within bounds
        # 2. Return character from buffer
    
    def __getitem__(self, index: int) -> str:
        """Support indexing with bounds checking."""
        return self.at(index)
    
    def __eq__(self, other: object) -> bool:
        """
        TODO: Compare two SafeStrings for equality.
        
        Args:
            other: Another SafeString or string
            
        Returns:
            True if contents are equal, False otherwise
        """
        # 1. Handle comparison with SafeString objects
        # 2. Handle comparison with Python strings
        # 3. Return False for other types
    
    def __add__(self, other: 'SafeString') -> 'SafeString':
        """
        TODO: Concatenate two SafeStrings.
        
        Args:
            other: Another SafeString to concatenate
            
        Returns:
            New SafeString containing concatenated result
            
        Raises:
            BufferOverflowError: If combined length exceeds capacity of result
        """
        # 1. Calculate combined length
        # 2. Create new SafeString with capacity = max(self.capacity, other.capacity)
        # 3. Copy self then other
        # 4. Return new SafeString
    
    def starts_with(self, prefix: str) -> bool:
        """
        TODO: Check if string starts with prefix.
        
        Args:
            prefix: Prefix to check
            
        Returns:
            True if string starts with prefix, False otherwise
            
        Raises:
            InvalidCharacterError: If prefix contains non-ASCII characters
        """
        # 1. Validate prefix is ASCII
        # 2. Check if prefix length <= self._length
        # 3. Compare characters
    
    def ends_with(self, suffix: str) -> bool:
        """
        TODO: Check if string ends with suffix.
        
        Args:
            suffix: Suffix to check
            
        Returns:
            True if string ends with suffix, False otherwise
            
        Raises:
            InvalidCharacterError: If suffix contains non-ASCII characters
        """
        # 1. Validate suffix is ASCII
        # 2. Check if suffix length <= self._length
        # 3. Compare characters from the end
    
    def replace(self, old: str, new: str) -> 'SafeString':
        """
        TODO: Replace all occurrences of old substring with new.
        
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
        # 2. Create new SafeString with same capacity
        # 3. Perform replacement
        # 4. Check length doesn't exceed capacity
        # 5. Return new SafeString
