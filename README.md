# SAMPLE_codesafe_challenge
A sample challenge built for the codesafe platform the we case studied in INF113

Python String Class implementation Challenge

Scenario: Building a Safe String Buffer for Network Protocols
You're working on a network security application that processes protocol data. Many network protocols have strict requirements about string handling
-Fixed buffer sizes, ASCII-only characters and bounds shecking are critical to prevent buffer overflow attacks and protocol violations. 
The standard Python str class is too permissive for this use case. It handles Unicode, has dynamic resizing, and doesn't enforce length limits. Your team needs a SafeString class that:

Enforces fixed capacity to match protocol field sizes

Validates character encoding (ASCII-only for many protocols)

Prevents buffer overflows with strict bounds checking

Provides explicit error handling for security-critical operations

Maintains immutability where appropriate to prevent accidental modification

You've been tasked to implement the core functionality with security as the primary concern.

# Use case/User story covering the challenge

As a cyber secuity student learning defensive programming techniques I want to implement a secure string buffer class so that I can practice writing security-critical code that prevents common attack vectors in networks and embedded systems.

Acceptance Criteria:
- Boundary Enforcement: The SafeString class must never allow writing beyond its fixed capacity, raising BufferOverflowError when capacity would be exceeded
- Input Validation: All string operations must validate that input contains only ASCII characters (0-127), raising InvalidCharacterError for violations
- Safe Indexing: Character access via at() method must perform bounds checking and raise IndexOutOfBoundsError for invalid indices

Story Points: 3
Point Rationale: This should be a strightforward and general string class implementation with error checking capabilities

Field	Description
Use Case Name	Complete Software and Security Related Challenges
Author	Jakob Groh
Priority	Critical
Source	10/14/25 Field Notes
Short Description	A student implements a security-focused string class with fixed capacity and ASCII validation to prevent buffer overflows and encoding attacks
Goals	Allows students to practice and master secure string parsing skills for software development and defensive cybersecurity
Primary Actor	Student
Secondary Actors	AI Tutor, Code Execution Environment
Preconditions	Student is logged into CodeSafe and has selected the Secure String Buffer challenge from the String Handling module
Success End Condition	All test cases pass and the completed flag is generated
Failed End Condition	Test cases fail or aren't run
Trigger	Student selects and clicks "Start" on the Secure String Buffer challenge
Basic Flow	1. Student selects challenge from String Handling module
2. System loads VS Code environment with starter code
3. Student implements missing methods with security constraints
4. Student runs test cases
5. System verifies all test cases pass
6. System marks challenge as complete and provides flag
Alternative Flow	Student leaves challenge before finishing; progress is saved automatically
Supplementary Information	Challenge focuses on defensive programming against common vulnerabilities (CWE-120 buffer overflows)
Estimated Time	30-60 minutes
Difficulty Level	Medium (requires understanding of security principles and multiple validation layers)
Open Issues	Determining optimal number of methods to implement; balancing educational value with complexity
