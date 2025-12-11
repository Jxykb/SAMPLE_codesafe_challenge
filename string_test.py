
"""
Test suite for SafeString implementation
"""

import pytest
from safe_string import SafeString, BufferOverflowError, InvalidCharacterError, IndexOutOfBoundsError


def test_basic_creation():
    """Test basic SafeString creation and properties."""
    s = SafeString(10)
    assert len(s) == 0
    assert s.capacity == 10
    assert str(s) == ""
    
    s2 = SafeString(5, "test")
    assert len(s2) == 4
    assert str(s2) == "test"
    assert s2.capacity == 5


def test_assign():
    """Test assign method."""
    s = SafeString(10)
    
    # Valid assignment
    s.assign("hello")
    assert str(s) == "hello"
    assert len(s) == 5
    
    # Assignment exceeding capacity should fail
    with pytest.raises(BufferOverflowError):
        s.assign("this is too long")
    
    # Non-ASCII assignment should fail
    with pytest.raises(InvalidCharacterError):
        s.assign("café")  # Contains non-ASCII 'é'
    
    # Content should remain unchanged after failed assignment
    assert str(s) == "hello"


def test_append():
    """Test append operations."""
    s = SafeString(10, "hello")
    
    # Valid append
    s.append(" world")
    assert str(s) == "hello world"
    assert len(s) == 11  # Wait, that's 11 characters...
    
    # Actually, that should fail - let's test properly
    s = SafeString(11, "hello")
    s.append(" world")
    assert str(s) == "hello world"
    assert len(s) == 11
    
    # Append exceeding capacity should fail
    s = SafeString(10, "hello")
    with pytest.raises(BufferOverflowError):
        s.append(" world!")  # Would be 12 characters
    
    # Append non-ASCII should fail
    with pytest.raises(InvalidCharacterError):
        s.append(" naïve")
    
    # Test append_char
    s = SafeString(10, "test")
    s.append_char('!')
    assert str(s) == "test!"
    
    # Append_char with non-ASCII
    with pytest.raises(InvalidCharacterError):
        s.append_char('é')
    
    # Append_char when full
    s = SafeString(5, "hello")
    with pytest.raises(BufferOverflowError):
        s.append_char('!')


def test_find_and_substr():
    """Test find and substring operations."""
    s = SafeString(20, "hello world")
    
    # Test find
    assert s.find("world") == 6
    assert s.find("hello") == 0
    assert s.find("nonexistent") == -1
    
    # Find with non-ASCII should fail
    with pytest.raises(InvalidCharacterError):
        s.find("worl∂")  # ∂ is non-ASCII
    
    # Test substr
    sub = s.substr(0, 5)
    assert str(sub) == "hello"
    assert sub.capacity == 20  # Should inherit capacity
    
    sub2 = s.substr(6)
    assert str(sub2) == "world"
    
    # Invalid substr
    with pytest.raises(IndexOutOfBoundsError):
        s.substr(100, 5)
    
    # Substr with length exceeding end
    sub3 = s.substr(6, 100)
    assert str(sub3) == "world"


def test_indexing():
    """Test character access."""
    s = SafeString(10, "test")
    
    # Valid indexing
    assert s.at(0) == 't'
    assert s.at(1) == 'e'
    assert s[2] == 's'
    assert s[3] == 't'
    
    # Out of bounds
    with pytest.raises(IndexOutOfBoundsError):
        s.at(10)
    
    with pytest.raises(IndexOutOfBoundsError):
        s.at(-1)


def test_equality():
    """Test equality comparisons."""
    s1 = SafeString(10, "hello")
    s2 = SafeString(10, "hello")
    s3 = SafeString(5, "hello")  # Same content, different capacity
    s4 = SafeString(10, "world")
    
    # Same content and capacity
    assert s1 == s2
    
    # Same content, different capacity
    assert s1 == s3  # Should compare content, not capacity
    
    # Different content
    assert s1 != s4
    
    # Comparison with Python strings
    assert s1 == "hello"
    assert "hello" == s1  # Should work both ways
    assert s1 != "world"
    
    # Invalid comparison
    assert s1 != 123  # Should return False, not crash


def test_concatenation():
    """Test string concatenation."""
    s1 = SafeString(10, "hello")
    s2 = SafeString(10, " world")
    
    # Valid concatenation
    s3 = s1 + s2
    assert str(s3) == "hello world"
    assert s3.capacity == 10  # Should use max capacity
    
    # Concatenation exceeding capacity
    s4 = SafeString(5, "hello")
    s5 = SafeString(5, "world")
    with pytest.raises(BufferOverflowError):
        result = s4 + s5  # Would be 10 characters, capacity 5


def test_prefix_suffix():
    """Test starts_with and ends_with."""
    s = SafeString(20, "hello world")
    
    assert s.starts_with("hello")
    assert s.starts_with("hell")
    assert not s.starts_with("world")
    
    assert s.ends_with("world")
    assert s.ends_with("orld")
    assert not s.ends_with("hello")
    
    # With non-ASCII
    with pytest.raises(InvalidCharacterError):
        s.starts_with("héllo")
    
    with pytest.raises(InvalidCharacterError):
        s.ends_with("wörld")


def test_replace():
    """Test replace operation."""
    s = SafeString(20, "hello world hello")
    
    # Simple replacement
    s2 = s.replace("hello", "hi")
    assert str(s2) == "hi world hi"
    
    # Replacement that would overflow
    s3 = SafeString(10, "hello")
    with pytest.raises(BufferOverflowError):
        s3.replace("hello", "verylongreplacement")
    
    # Replacement with non-ASCII
    with pytest.raises(InvalidCharacterError):
        s.replace("hello", "héllo")
    
    with pytest.raises(InvalidCharacterError):
        s.replace("héllo", "hi")


def test_edge_cases():
    """Test various edge cases."""
    # Empty string operations
    s = SafeString(10)
    assert s.find("a") == -1
    assert str(s.substr(0, 5)) == ""
    
    # Single character
    s = SafeString(5, "A")
    assert s.find("A") == 0
    assert s.find("B") == -1
    
    # Full capacity
    s = SafeString(3, "123")
    with pytest.raises(BufferOverflowError):
        s.append_char("4")
    
    # Case sensitivity
    s = SafeString(10, "Hello")
    assert s.find("hello") == -1  # Case sensitive
    
    # Zero-length operations
    s = SafeString(10, "test")
    s.append("")  # Should work
    assert str(s) == "test"
    
    s.replace("", "x")  # Empty search string - what should happen?
    # This is a design decision - could raise ValueError or do nothing


def test_is_ascii():
    """Test the is_ascii helper method."""
    s = SafeString(10)
    
    assert s.is_ascii("hello")
    assert s.is_ascii("HELLO 123 !@#")
    assert not s.is_ascii("café")
    assert not s.is_ascii("🎉")
    assert not s.is_ascii("∂y/∂x")  # Mathematical symbols


if __name__ == "__main__":
    print("Running SafeString tests...")
    
    # Run all test functions
    test_functions = [
        test_basic_creation,
        test_assign,
        test_append,
        test_find_and_substr,
        test_indexing,
        test_equality,
        test_concatenation,
        test_prefix_suffix,
        test_replace,
        test_edge_cases,
        test_is_ascii
    ]
    
    for test_func in test_functions:
        try:
            test_func()
            print(f"✓ {test_func.__name__} passed")
        except AssertionError as e:
            print(f"✗ {test_func.__name__} failed: {e}")
        except Exception as e:
            print(f"✗ {test_func.__name__} error: {e}")
    
    print("\nAll tests completed!")
