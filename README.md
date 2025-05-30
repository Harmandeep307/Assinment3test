# Assinment3test
1. Single Responsibility Principle (SRP)
Each function in my program is designed to perform one specific task. For instance, the function that handles approval validation is separate from the one that prints information. Similarly, functions related to displaying data are distinct from those that handle calculations or validations, ensuring that each component focuses on a single responsibility.

2. Open/Closed Principle
The code is structured to allow easy addition of new features without altering existing ones. For example, I can introduce new approval rules by writing new functions, leaving the existing logic unchanged. This enhances maintainability and scalability.

3. Keep It Simple, Stupid (KISS)
I focused on simplicity by writing short, easy-to-understand functions. Conditions such as checking whether a total is under a certain threshold are implemented using clear and direct if statements, avoiding unnecessary complexity.

4. Composition Over Inheritance
Although the program does not use classes, I applied the principle by dividing the program into small, reusable components. Instead of grouping logic into large blocks, I created modular functions that can be reused in different parts of the application.

5. Separation of Concerns
Each script or function has a clear and specific purpose—whether it’s handling approvals, displaying information, processing input, or performing calculations. This separation makes the code easier to understand, debug, and modify, as changes in one area do not affect others.

6. Don’t Repeat Yourself (DRY)
Repeated logic was eliminated by creating shared functions. For example, there is one centralized function to handle the printing of requisition details. Any updates to the print format only need to be made in this one location, ensuring consistency and reducing redundancy.

7. You Aren’t Gonna Need It (YAGNI)
The code only includes the features required for its current purpose. I avoided adding unnecessary functions or unused variables. This kept the program lean and focused on delivering exactly what was needed.

8. Avoid Premature Optimization
I first ensured that the program worked correctly before attempting any performance enhancements. After verifying its functionality, I then focused on improving the structure and readability of the code to make it more maintainable.

9. Refactoring and Clean Code
Once the initial version was complete, I revisited the code to improve its structure. I removed redundant lines, chose meaningful names for variables and functions, and reorganized parts of the code to enhance clarity and maintain a clean layout.
