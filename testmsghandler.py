import string

class Handler:

	def sum_from_text(self):
		nums = [int(s) for s in self.text.split() if s.isdigit()]
		if nums:
			answer, i = 0, 0
			while i < len(nums):
				answer += nums[i]
				i += 1
		else:
			answer = "Not solvable, please try again"
		return answer

	def math_eval_text(self):
		symbols = '^*()/+-'
		formula = [(x,self.text.index(x)) for x in self.text if x in string.digits+symbols]
		result = eval(''.join(x[0] for x in formula), {'__builtins__':None})
		return "The answer to " + ''.join(x[0] for x in formula) + " is " + str(result)

	def process(self):
		nums = [int(s) for s in self.text.split() if s.isdigit()]
		if nums:
			return self.math_eval_text()
		else:
			return "enter an expression please"

	def __init__(self, str):
		self.text = str


