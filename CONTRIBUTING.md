# Contributing Guidelines

## Adding New Problems

When adding a new DSA problem:

1. **File Structure**: Place in appropriate directory
   - Arrays/Strings → `dsa/arrays_strings/`
   - Trees → `dsa/trees/`
   - Graphs → `dsa/graphs/`
   - etc.

2. **Code Format**:
   ```python
   """
   Problem Name - LeetCode #XXX
   Frequency: X% (Description)
   
   Problem description...
   
   Time Complexity: O(...)
   Space Complexity: O(...)
   """
   
   from typing import List
   
   def solution(nums: List[int]) -> int:
       """Solution with comments"""
       pass
   
   # Test cases
   if __name__ == "__main__":
       # Test cases here
       pass
   ```

3. **Include**:
   - Multiple approaches (brute force → optimal)
   - Time/space complexity analysis
   - Test cases with expected outputs
   - Clear comments

## Testing

- Add unit tests in `tests/` directory
- Use pytest for testing
- Run tests: `pytest tests/ -v`

## Code Style

- Use type hints
- Follow PEP 8
- Add docstrings
- Include complexity analysis

## Documentation

- Update README.md if adding major features
- Update QUICK_REFERENCE.md for new patterns
- Keep LEARNING_ROADMAP.md updated

Thank you for contributing! 🚀

