from solution.extractor import Solution

# Initialize
sol = Solution()

while True:
    inp = input("Enter address (or 'exit'): ")
    if inp.strip().lower() == 'exit':
        break
    result = sol.process(inp)
    print("Extracted:")
    print(result)
