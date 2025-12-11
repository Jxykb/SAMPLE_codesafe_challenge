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

Use Case Name | Complete Software and Secuirty Realted challenges
Author        | Jakob Groh
Priority      | Critical
Source        | 10/14/25
Short Desc.   | A student can complete this string class challenge by writing code in the VS code environment and pass all test cases
Goals         | Allows students to practice and master string parsing skills for software development
Primary Actor | Student
Secondary     | N.A
Preconditions | The student is loged in and selected the respective challenge
Succes End    | All test cases pass and the completed flag is generated
Failed End    | Test cases fail or arent run
Trigger       | The student selects and then clicks start on this specific challenge
Basic Flow    | Student selects this challenge from the string module, system load the built in environment and the starter code, the system verifies all tets cases pass. the system marks the challenge as complete and provides the flag
Alternate     | Student leaves the challenge before finishing in which the students progress is saved
Sup Info      | Assumed there is already a string module 
Open Issues   | How many functions should the user implement, even though theyre simple is this too much?
