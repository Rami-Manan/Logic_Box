print ("HELLO! Welcome to the Pattern Generator and Number Analyzer!")

while True:
	print()
	print("Select an option:")
	print("1. Generate a Pattern")
	print("2. Analyze a Range of Numbers")
	print("3. Exit")
	print()

	choice = int(input("Enter your choice: "))

	if choice == 1:
		while True:
			rows = int(input("Enter the number of rows for the pattern: "))

			if rows <= 0:
				print()
				print("Invalid input!")
				print("Number of rows must be a positive integer.")
				continue
			else:
				
				pass
				break

		print()
		print("Pattern:")

		
		for row in range(1, rows + 1):
			for star in range(row):
				print("*", end="")
			print()

	elif choice == 2:
		while True:
			print()
			start = int(input("Enter the start of the range: "))
			end = int(input("Enter the end of the range: "))

			if end < start:
				print()
				print("Invalid range!")
				print("The end number must be greater than or equal to the start number.")
				continue
			else:
				break

		print()
		total = 0

		for number in range(start, end + 1):
			if number % 2 == 0:
				print("Number", number, "is Even")
			else:
				print("Number", number, "is Odd")

			total = total + number

		print()
		print("Sum of all numbers from", start, "to", end, ":", total)

	elif choice == 3:
		print()
		print("===============================================")
		print("Thank you for using the Pattern Generator")
		print("and Number Analyzer!")
		print("Exiting the program. Goodbye!")
		print("===============================================")
		break

	else:
		print()
		print("Invalid choice!")
		print("Please select 1, 2, or 3.")
		continue
