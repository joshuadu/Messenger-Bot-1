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

	def process(self):
		self.sum_from_text()

	def __init__(self, str):
		self.text = str


